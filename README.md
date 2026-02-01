# 📧 Automated Gmail Spam Detection System

An automated system that connects to a user’s Gmail account, fetches emails using the Gmail API, and classifies them as **Spam** or **Not Spam (Ham)** using a **Machine Learning (Naive Bayes)** model.

This project is designed as a **portfolio-ready project for beginners/freshers** to demonstrate skills in Python, Machine Learning, NLP, and API integration.

---

## 🎯 Project Objective

- Authenticate a user with their Gmail account (OAuth 2.0)
- Fetch recent emails from Gmail
- Classify emails as Spam or Ham using ML
- Display results in the terminal
- Log detected spam emails for review

---

## 🧠 Skills Demonstrated

- Python programming
- Machine Learning (Naive Bayes)
- Natural Language Processing (TF-IDF)
- Gmail API & OAuth 2.0
- Project structuring
- Git & GitHub workflow

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **ML / NLP:** Scikit-learn
- **Data Handling:** Pandas
- **API:** Gmail API
- **Authentication:** Google OAuth 2.0
- **Model Saving:** Joblib

---

## 📁 Project Structure

'''text
automated-gmail-spam-detection/
│
├── main.py # Main entry point
├── spam_model.py # ML model training script
├── requirements.txt # Project dependencies
├── credentials.json # Google OAuth credentials (ignored by git)
│
├── data/
│ └── spam.csv # Dataset
│
├── utils/
│ └── gmail_utils.py # Gmail API helper functions
│
├── models/
│ ├── spam_model.pkl # Trained ML model
│ └── .gitkeep
│
├── logs/
│ ├── spam_logs.txt # Logged spam emails
│ └── .gitkeep
│
└── README.md
 '''

---

## 📊 Dataset

- **Source:** Kaggle – SMS Spam Collection Dataset
- **Columns Used:**
  - `Category` → spam / ham
  - `Message` → text content

The dataset is used to train a **TF-IDF + Multinomial Naive Bayes** classifier.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/automated-gmail-spam-detection.git
cd automated-gmail-spam-detection



2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Gmail API Configuration

Create a project in Google Cloud Console

Enable Gmail API

Create OAuth Client ID

Download credentials.json

Add your Gmail ID as a Test User

Scope used:

https://www.googleapis.com/auth/gmail.readonly

🏋️ Train the Machine Learning Model
python spam_model.py


Expected output:

Model trained successfully
spam_model.pkl created

▶️ Run the Application
python main.py

✅ Sample Output
Fetching emails...

[SPAM]
From   : alert@unknown.com
Subject: Security alert
---------------------------------

[HAM]
From   : GitHub <noreply@github.com>
Subject: OAuth application added
---------------------------------

🧾 Spam Logging

Detected spam emails are saved in:

logs/spam_logs.txt


Format:

FROM: sender_email | SUBJECT: email_subject

🔒 Security Notes

Gmail access is read-only

OAuth credentials are not committed to GitHub

Project runs locally

No email content is modified or deleted

🚀 Future Enhancements

Analyze full email body

Auto-move spam to Gmail Spam folder

Sender blocking

GUI using Tkinter or Streamlit

Improved model accuracy

👤 Author

Dhruv Kashyap
📧 dhruv.kashyap.tech@gmail.com

⭐ Acknowledgements

Google Gmail API

Kaggle SMS Spam Dataset

Scikit-learn Documentation