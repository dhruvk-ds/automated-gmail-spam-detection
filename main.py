from utils.gmail_utils import gmail_login, fetch_emails
import joblib

def main():
    print("Logging into Gmail...")
    service = gmail_login()

    print("Fetching emails...")
    emails = fetch_emails(service, max_results=10)

    model = joblib.load('models/spam_model.pkl')

    print("\nSpam Detection Results:\n")

    with open('logs/spam_logs.txt', 'a', encoding='utf-8') as log:
        for email in emails:
            text_to_check = email['subject']

            if not text_to_check.strip():
                continue

            prediction = model.predict([text_to_check])[0]

            print(f"[{prediction.upper()}]")
            print(f"From   : {email['sender']}")
            print(f"Subject: {email['subject']}")
            print("-" * 50)

            if prediction.lower() == 'spam':
                log.write(
                    f"FROM: {email['sender']} | SUBJECT: {email['subject']}\n"
                )

if __name__ == "__main__":
    main()
