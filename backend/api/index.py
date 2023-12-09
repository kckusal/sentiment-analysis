from flask import Flask, request
import ml

app = Flask(__name__)

@app.route('/')
def home():
  return 'Hello, World!'

@app.route('/about')
def about():
  return 'About'

@app.post('/api/evaluate-sentiment')
def evaluate_sentiment():
  body = request.get_json()
  
  if 'input_text' in body:
    return ml.predict([body['input_text']])
  else:
    return 'Bad request: The HTTP request must have the Content-Type: "application/json" and contain "input_text" param in body.', 400