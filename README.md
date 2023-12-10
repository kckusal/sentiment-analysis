# About

This is a sentiment analysis NLP project done as part of Intelligent Systems course offered at Torrens University Australia.

# Project Team Members

- Felix Wang
- Sunil Chaudhary
- Kusal KC

# Training Dataset

The training dataset was taken from [https://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html](https://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html). _This Multi-Domain Sentiment Dataset contains product reviews taken from Amazon.com from 4 product types (domains): Kitchen, Books, DVDs, and Electronics._

# Training an ML model

The model training information can be found in the [attached .ipynb notebook file](https://github.com/kckusal/sentiment-analysis/blob/main/ISY501_NLP_Project_Sentiment_Analysis.ipynb). The trained model was saved for later use.

# Deploying the model

The trained model has been deployed online. The backend is a Flask app serving the model's predictions via a `POST /api/evaluate-sentiment` endpoint. The code for this Flask app can be found in __/backend__ directory. The service is deployed with [railway.app](https://railway.app) and available at [https://sentiment-analysis-production-7796.up.railway.app](https://sentiment-analysis-production-7796.up.railway.app).

There's a frontend application as well which provides us an interface to input text and get predictions regarding the sentiment using this model. You can try the interface yourself at [https://sentiment-analysis-frontend-kusal.vercel.app](https://sentiment-analysis-frontend-kusal.vercel.app).
