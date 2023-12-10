import os
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pickle import load

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

port = os.environ['PORT']
print("PORT = {}".format(port))

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Construct the path to the files
preprocessing_info_file_path = os.path.join(current_dir, 'preprocessing_info.pkl')
model_file_path = os.path.join(current_dir, 'sentiment_analyzer.h5')

# Load preprocessing parameters
with open(preprocessing_info_file_path, "rb") as pkl_file:
    preprocessing_info = load(pkl_file)

tokenizer = Tokenizer()
tokenizer.word_index = preprocessing_info['word_index']
tokenizer.num_words = preprocessing_info['num_words']
max_len = preprocessing_info["max_len"]

# Load model
model = load_model(model_file_path)

def clean_review_text(text: str) -> list:
    # Remove <review_text> at start and </review_text> at end
    sentence = re.sub(r'<review_text>', '', text)
    sentence = re.sub(r'</review_text>', '', sentence)

    # Remove punctuations
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Convert to lowercase and tokenize
    tokens = word_tokenize(sentence.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return lemmatized_tokens

def predict(review_texts: list) -> list:
    # Clean and preprocess each review text
    preprocessed_reviews = [clean_review_text(text) for text in review_texts]

    # Convert preprocessed text to sequences using the tokenizer used during training
    sequences = tokenizer.texts_to_sequences(preprocessed_reviews)

    # Pad sequences to have consistent length
    padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')

    # Make predictions using the loaded model
    predictions = model.predict(padded_sequences)
    
    # Convert predictions to a list and get only first value from result item
    prediction_values = [item[0] for item in predictions.tolist()]

    results = []
    for i, prediction in enumerate(prediction_values):
      label = 'Positive' if prediction > 0.5 else 'Negative'
      input_text = review_texts[i]
      accuracy = round(float(prediction), 8)

      result_dict = { 'label': label, 'accuracy': accuracy, 'input_text': input_text }
      results.append(result_dict)
    
    return results