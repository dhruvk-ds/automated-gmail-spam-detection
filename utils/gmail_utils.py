from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def gmail_login():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',
        SCOPES
    )
    creds = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=creds)
    return service


def fetch_emails(service, max_results=10):
    emails = []

    results = service.users().messages().list(
        userId='me', maxResults=max_results
    ).execute()

    messages = results.get('messages', [])

    for msg in messages:
        msg_data = service.users().messages().get(
            userId='me', id=msg['id'], format='metadata',
            metadataHeaders=['Subject', 'From']
        ).execute()

        subject = ""
        sender = ""

        headers = msg_data.get('payload', {}).get('headers', [])
        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
            elif header['name'] == 'From':
                sender = header['value']

        emails.append({
            "sender": sender,
            "subject": subject
        })

    return emails
