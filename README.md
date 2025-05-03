# Support Ticket Mood Logger

A Streamlit application for logging and visualizing the mood of support tickets.

## Features

- Log support ticket moods with emojis and optional notes
- View today's mood entries in a table
- Visualize mood distribution with an interactive Plotly chart
- Automatic timestamp tracking
- Google Sheets integration for data storage

## Local Development

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.streamlit/secrets.toml` file with your Google Sheets credentials
4. Run the application:
   ```bash
   streamlit run mood_logger.py
   ```

## Deployment to Streamlit Community Cloud

1. Fork this repository
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/)
3. Click "New app"
4. Select your forked repository
5. Set the main file path to `mood_logger.py`
6. Add your Google Sheets credentials in the app's settings:
   - Go to "Settings" > "Secrets"
   - Copy the contents of your `.streamlit/secrets.toml` file
   - Click "Save"
7. Click "Deploy"

## Usage

1. Select a mood emoji from the dropdown
2. Add an optional note about the ticket
3. Click "Log Mood" to save the entry
4. View today's entries and mood distribution below

## Requirements

- Python 3.8+
- Streamlit
- gspread
- google-auth
- pandas
- plotly

## Note

This application uses a shared Google Sheet for data storage. All users will log their moods to the same sheet. The app owner needs to set up the Google Sheets API credentials in the Streamlit secrets.

You can view the shared Google Sheet here: [Support Ticket Mood Log](https://docs.google.com/spreadsheets/d/11-APIrn4RxLYfSoXNIfVlQjv-djMjCtGSm-qlZtDCqg/edit?gid=0#gid=0)

## License

MIT 