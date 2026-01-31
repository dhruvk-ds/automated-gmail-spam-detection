import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

def train_model():
    # Load Kaggle dataset
    df = pd.read_csv('data/spam.csv')

    print("Dataset columns:", df.columns.tolist())

    # Rename columns to standard names
    df = df[['Category', 'Message']]
    df.columns = ['label', 'text']

    # Remove missing values
    df.dropna(inplace=True)

    X = df['text']
    y = df['label']

    model = Pipeline([
        ('vectorizer', CountVectorizer(stop_words='english')),
        ('classifier', MultinomialNB())
    ])

    model.fit(X, y)

    joblib.dump(model, 'models/spam_model.pkl')
    print("Spam model trained successfully using Kaggle dataset")

if __name__ == "__main__":
    train_model()
