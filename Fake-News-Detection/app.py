# app.py

from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('fake_news_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news_text = request.form.get('news_text')
    prediction = model.predict([news_text])[0]
    
    if prediction == 0:
        result = "This news is likely REAL."
    else:
        result = "This news is likely FAKE."
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
