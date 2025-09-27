from __future__ import print_function
import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail API scope: read-only access to emails
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    creds = None

    # Load saved token from previous authentication
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no valid credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Build the Gmail API service
    service = build('gmail', 'v1', credentials=creds)

    # Get the latest 5 messages
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
    else:
        print('Latest messages:')
        for msg in messages:
            msg_data = service.users().messages().get(
                userId='me', id=msg['id']).execute()
            for header in msg_data['payload']['headers']:
                if header['name'] == 'Subject':
                    print(f"- {header['value']}")


if __name__ == '__main__':
    main()
