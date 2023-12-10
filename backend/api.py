from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import ml
import sys
import pkg_resources

port = os.environ['PORT']
os.environ['TF_CPP_MIN_LOG_LEVEL'] = 2

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
    # return []
  else:
    return 'Bad request: The HTTP request must have the Content-Type: "application/json" and contain "input_text" param in body.', 400

@app.route('/version')
def version_info():
  python_version = sys.version
  installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

  info = {
      'Python Version': python_version,
      'Installed Packages': installed_packages
  }

  return jsonify(info)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port, use_reloader=False)

def create_app():
  print('PORT is {}'.format(port))
  return app