from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load('D:\phisMe\phishing.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data sent in the request
    data = request.get_json()

    if not data or 'url' not in data:
        return jsonify({'prediction': 'URL not provided.'}), 400
    
    url = data['url']
    
    
    prediction = model.predict([url])
    print(f"URL: {url}, Prediction: {prediction}")
    print(f"Prediction type: {type(prediction)}")
    print(f"Prediction shape: {prediction.shape}")
    print(f"Prediction value: {prediction[0]}")
    if prediction[0] == "bad":
        print("Phishing detected!")
        result = "⚠️ Phishing Website Detected!"
    
    else:
        print("Legitimate website detected!")
        result = "✅ Legitimate Website"

    # result = "⚠️ Phishing Website Detected!" if prediction[0] == "bad" else "✅ Legitimate Website"


    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
