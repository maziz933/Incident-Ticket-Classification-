import re
import string
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

class EmailClassifier:
    def __init__(self, model_path, tokenizer_path, max_text_len):
        self.model = load_model(model_path)
        with open(tokenizer_path, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        self.max_text_len = max_text_len

    def preprocess_text(self, text):
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        # Tokenize and pad
        tokens = self.tokenizer.texts_to_sequences([text])
        tokens_pad = pad_sequences(tokens, maxlen=self.max_text_len, padding='post')
        return tokens_pad

    def classify(self, text):
        preprocessed_text = self.preprocess_text(text)
        prediction = self.model.predict(preprocessed_text)
        return prediction[0]
