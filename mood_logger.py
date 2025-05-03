import streamlit as st
import gspread
from google.oauth2 import service_account
import datetime
import os
import pandas as pd
import plotly.express as px


# Set page config
st.set_page_config(
    page_title="Support Mood Logger",
    page_icon="📝",
    layout="centered"
)

# App title and description
st.title("📝 Support Ticket Mood Logger")
st.markdown("""
Log the mood of support tickets to help track customer sentiment.
""")

# Create two columns for the form
col1, col2 = st.columns(2)

with col1:
    # Emoji selection
    mood_emoji = st.selectbox(
        "Select the mood of the ticket",
        options=['😊 Happy', '😐 Neutral', '😔 Sad', '😡 Angry', '🎉 Excited', '😕 Confused'],
        format_func=lambda x: x.split()[0]  # Show only emoji in dropdown
    )

with col2:
    # Optional note
    note = st.text_area(
        "Add an optional note",
        placeholder="Enter any additional context about the ticket mood...",
        height=100
    )

# Add a submit button
if st.button("Log Mood", type="primary"):
    try:
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create a new row
        new_row = [timestamp, mood_emoji.split()[0], note if note else "No note provided"]
        
        # Set up credentials using Streamlit secrets
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        
        # Get credentials from Streamlit secrets
        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=scope
        )
        
        # Open the sheet and append the row
        gc = gspread.authorize(credentials)
        sh = gc.open_by_key(st.secrets["google_sheets"]["spreadsheet_id"])
        worksheet = sh.sheet1  # Use the first sheet
        worksheet.append_row(new_row)
        
        st.success("✅ Mood logged successfully!")
        
        # Show a preview of what was logged
        st.info(f"""
        **Logged Entry:**
        - Time: {timestamp}
        - Mood: {mood_emoji.split()[0]}
        - Note: {note if note else "No note provided"}
        """)
        
    except Exception as e:
        st.error(f"❌ Error logging mood: {str(e)}")

# Show today's entries and mood distribution
try:
    # Get all data from the sheet
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    
    if not df.empty:
        # Convert timestamp to datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df['Date'] = df['Timestamp'].dt.date
        
        # Get today's date
        today = datetime.date.today()
        
        # Filter for today's entries
        today_df = df[df['Date'] == today]
        
        if not today_df.empty:
            st.subheader("Today's Entries")
            st.dataframe(today_df.sort_values('Timestamp', ascending=False))
            
            # Create mood count histogram
            mood_counts = today_df['Mood'].value_counts().reset_index()
            mood_counts.columns = ['Mood', 'Count']
            
            fig = px.bar(
                mood_counts,
                x='Mood',
                y='Count',
                title='Today\'s Mood Distribution',
                color='Mood',
                text='Count'
            )
            
            # Customize the layout
            fig.update_layout(
                showlegend=False,
                xaxis_title='Mood',
                yaxis_title='Number of Entries',
                height=400
            )
            
            # Display the plot
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No entries for today yet. Start logging moods to see them here!")
            
except Exception as e:
    st.info("No entries yet. Start logging moods to see them here!") 