from flask import Flask, render_template, request
from model.classifier import EmailClassifier
from model.preprocess import preprocess_message, abv_lng, abv_arb, abv_tech
app = Flask(__name__)

# Paths to the model and the tokenizer
MODEL_PATH = "model/cnn_bigru.keras"
TOKENIZER_PATH = "model/tokenizer.pkl"

# defines the maximum length of the input text processed by the model
MAX_TEXT_LEN = 50


# initialize the classifier
classifier = EmailClassifier(MODEL_PATH, TOKENIZER_PATH, MAX_TEXT_LEN)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/email_entrants')
def email_entrants():
    return render_template('email_entrants.html')
@app.route('/predict', methods=['POST'])
def predict():
    email_content = request.form['email_content']
    
    # Preprocess the email content
    preprocessed_content = preprocess_message(email_content, 'fr')  # Change 'fr' to 'eng' if the email is in English.
    
    # classify the preprocessed content
    prediction = classifier.classify(preprocessed_content)
    
    print(f"Prediction: {prediction}")  # Add a debug line to print the prediction in the console.
    return render_template('prediction.html', prediction=prediction, email_content=email_content)


if __name__ == '__main__':
    app.run(debug=True)





