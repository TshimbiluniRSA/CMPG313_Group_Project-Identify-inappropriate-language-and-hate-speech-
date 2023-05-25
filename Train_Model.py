import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import joblib

def train_model(data_files, model_file, vectorizer_file):
    # Load the datasets
    data = pd.concat([pd.read_csv(file) for file in data_files])

    # Preprocessing
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data["clean_tweet"])
    y = data["class"]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train the model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, model_file)

    # Save the vectorizer
    joblib.dump(vectorizer, vectorizer_file)

    # Evaluate the model
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print("Classification Report:")
    print(report)

# Train the model with cleaned_tweets.csv and cleaned_labeled_data1.csv
data_files = ["cleaned_tweets.csv", "cleaned_labeled_data1.csv"]
train_model(data_files, "trained_model_combined.joblib", "vectorizer_combined.joblib")
