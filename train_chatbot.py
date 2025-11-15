import json
import pickle
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Download tokenizer
nltk.download('punkt')

# Load intents
with open('intents.json') as file:
    data = json.load(file)

# Prepare data
corpus = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern.lower())
        labels.append(intent['tag'])

# Preprocess and Vectorize
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
X = vectorizer.fit_transform(corpus)

# Train classifier
clf = LogisticRegression()
clf.fit(X, labels)

# Save model and vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ Model training complete and saved.")
