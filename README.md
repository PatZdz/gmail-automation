# Gmail Automation
Python, GCP, Gmail API - The program allows you to sort emails, backup attachments to the cloud or locally, and gives you the ability to report emails. This is especially useful in large organizations where there is a huge amount of emails per day.

🛠️ Tech:
- Python
- GCP
- google-api-python-client
- google-auth-oauthlib
- google-auth-httplib2 

✅ What does it do?:
- Connects to Gmail API using OAuth2 authentication
- Retrieves the latest 5 email messages
- Displays email subjects in the console
- Provides a foundation for email automation tasks

## Setup Instructions

### 1. Google Cloud Console Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API for your project
4. Go to "Credentials" and create OAuth 2.0 Client IDs
5. Download the credentials JSON file

### 2. Project Setup
1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
   ```
3. Replace the placeholder values in `credentials.json` with your actual Google OAuth2 credentials:
   - `client_id`: Your OAuth2 client ID
   - `client_secret`: Your OAuth2 client secret  
   - `project_id`: Your Google Cloud project ID

### 3. Running the Application
1. Run the script:
   ```bash
   python main.py
   ```
2. On first run, it will open a browser window for OAuth2 authentication
3. Grant the necessary permissions
4. The authentication token will be saved for future runs

### 4. Security Notes
- Never commit `token.json` or real `credentials.json` to version control
- The current `credentials.json` contains placeholder values - replace them with your actual credentials
- Keep your OAuth2 credentials secure and don't share them publicly

🤓 What I learned?:
- How to integrate with Gmail API using Python
- OAuth2 authentication flow implementation
- Secure handling of API credentials
- Email data processing and extraction

tl;dr:
This program connects to Gmail API, authenticates using OAuth2, and retrieves the latest email messages for processing and automation tasks.
