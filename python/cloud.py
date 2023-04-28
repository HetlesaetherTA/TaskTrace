from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path

SCOPES = ['https://www.googleapis.com/auth/drive']

class Account:
    creds = None
    def login():
    
        if os.path.exists("token.json"):
            global creds
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    def initiate():
        service = build("drive", "v3", credentials=creds)

        file_metadata = {
            'name': 'TaskTrace',
            'mimeType': 'application/vnd.google-apps.folder'
        }
        service.files().create(body=file_metadata).execute()
Account.login()
Account.initiate()
