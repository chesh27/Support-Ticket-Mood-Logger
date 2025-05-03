# Support Ticket Mood Logger

A Streamlit application for logging and visualizing the mood of support tickets.

## Features

- Log support ticket moods with emojis and optional notes
- View today's mood entries in a table
- Visualize mood distribution with an interactive Plotly chart
- Automatic timestamp tracking
- Google Sheets integration for data storage

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Google Sheets API:
   - Create a project in Google Cloud Console
   - Enable Google Sheets API
   - Create a service account and download credentials.json
   - Place credentials.json in the project directory
   - Share your Google Sheet with the service account email

4. Run the application:
   ```bash
   streamlit run mood_logger.py
   ```

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

## License

MIT 