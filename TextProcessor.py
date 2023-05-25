from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load("trained_model_combined.joblib")
vectorizer = joblib.load("vectorizer_combined.joblib")

# Define the home page
@app.route("/")
def home():
    return render_template("index.html")

# Define the API endpoint for classification
@app.route("/classify", methods=["POST"])
def classify_text():
    text = request.json["text"]
    processed_text = vectorizer.transform([text])
    class_label = model.predict(processed_text)[0]
    if class_label == 0:
        result = "Hate Speech"
    elif class_label == 1:
        result = "Offensive Language"
    else:
        result = "Neither"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
