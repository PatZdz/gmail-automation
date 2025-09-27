from __future__ import print_function
import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Zakres dostępu: tylko odczyt maili
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    creds = None

    # Token zapisany po pierwszym logowaniu
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Jeśli nie ma tokena, użytkownik musi się zalogować
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Zapisz token do pliku
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Połącz się z Gmail API
    service = build('gmail', 'v1', credentials=creds)

    # Pobierz najnowsze 5 wiadomości
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    if not messages:
        print('Brak wiadomości.')
    else:
        print('Ostatnie wiadomości:')
        for msg in messages:
            msg_data = service.users().messages().get(
                userId='me', id=msg['id']).execute()
            for header in msg_data['payload']['headers']:
                if header['name'] == 'Subject':
                    print(f"- {header['value']}")


if __name__ == '__main__':
    main()
