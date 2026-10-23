
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


# Step 1: Create the dataset
data = {
    "message": [
        "Congratulations you won a free prize",
        "Claim your free cash reward now",
        "Win money now click this link",
        "Urgent claim your free gift",
        "You have won a lottery prize",
        "Get free entry in our contest",
        "Limited offer win cash today",
        "Free voucher waiting claim now",
        "Hey are we still meeting today",
        "Can you send me the notes",
        "Please call me when you arrive",
        "Are you coming to class tomorrow",
        "Thanks for helping me yesterday",
        "Let's have lunch after class",
        "I will send the project file",
        "Can we meet at the library"
    ],
    "label": [
        "spam", "spam", "spam", "spam",
        "spam", "spam", "spam", "spam",
        "ham", "ham", "ham", "ham",
        "ham", "ham", "ham", "ham"
    ]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df.head())
print("\nLabel counts:")
print(df["label"].value_counts())


# Step 2: Separate features and labels
X = df["message"]
y = df["label"]


# Step 3: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\nTraining messages:", len(X_train))
print("Testing messages:", len(X_test))


# Step 4: Convert text into TF-IDF features
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("\nTraining TF-IDF shape:", X_train_tfidf.shape)
print("Testing TF-IDF shape:", X_test_tfidf.shape)


# Step 5: Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

print("\nNaive Bayes model trained successfully!")


# Step 6: Evaluate the model
y_pred = model.predict(X_test_tfidf)

print("\nActual labels:", y_test.tolist())
print("Predicted labels:", y_pred.tolist())

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))


# Step 7: Predict new messages
new_messages = [
    "Congratulations claim your free prize now",
    "Hey are we meeting after class",
    "Win cash now with this special offer",
    "Please send me the project notes"
]

new_messages_tfidf = vectorizer.transform(new_messages)
new_predictions = model.predict(new_messages_tfidf)

print("\nNew Message Predictions:")

for message, prediction in zip(new_messages, new_predictions):
    print(f"Message: {message}")
    print(f"Prediction: {prediction}")
    print("-" * 40)
