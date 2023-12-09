from flask import Flask, request
from flask_cors import CORS, cross_origin
import ml

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
  return 'Hello, World!'

@app.route('/about')
def about():
  return 'About'

@app.post('/api/evaluate-sentiment')
@cross_origin()
def evaluate_sentiment():
  body = request.get_json()
  
  if 'input_text' in body:
    predictions = ml.predict([body['input_text']])
    return predictions[0]
  else:
    return 'Bad request: The HTTP request must have the Content-Type: "application/json" and contain "input_text" param in body.', 400