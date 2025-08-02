import re
import string
import spacy
import pandas as pd
from nltk.corpus import stopwords
# from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Load lemmatization models for English and French
nlp_en = spacy.load('en_core_web_sm')
nlp_fr = spacy.load('fr_core_news_sm')

# Load abbreviations
abv_lng = pd.read_csv('model/abv_lng.csv')
abv_arb = pd.read_csv('model/abv_arb.csv')
abv_tech = pd.read_csv('model/abv_tech.csv')

# Function to capture text before a delimiter
def capturer_texte_avant_delimiteur(texte, delimiter):
    match = re.search(delimiter, texte, re.IGNORECASE)
    if match:
        index_delimiteur = match.start()
        texte_avant = texte[:index_delimiteur].strip()
        return texte_avant, index_delimiteur
    else:
        return texte.strip(), -1

# Function to clean images
def nettoyer_images(texte):
    texte = re.sub(r'\[cid:.*?\]', ' @image ', texte)
    texte = re.sub(r'\[image: .*?\]', ' @image ', texte)
    texte = re.sub(r'<img .*?>', ' @image ', texte)
    texte = re.sub(r'<img .*?/>', ' @image ', texte)
    texte = re.sub(r'<img .*? >', ' @image ', texte)
    return texte.strip()

# Function to replace ping statistics
def replace_Ping_Stats(message):
    ping_stats_patterns = [
        r'\d+% packet loss, time \d+ms rtt min/avg/max/mdev = [\d.]+/[\d.]+/[\d.]+/[\d.]+ ms',
        r'\d+ packets transmitted, \d+ received, \d+% packet loss, time \d+ms',
        r'(\d+) packets transmitted, (\d+) packets received, (\d+)% packet loss',
        r'(\d+)% packet loss'
    ]
    for pattern in ping_stats_patterns:
        message = re.sub(pattern, '@StatPing', message)
    return message

# Function to replace email addresses
def replace_emails(message):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    cleaned_message = re.sub(email_pattern, ' @email', message)
    return cleaned_message

# Function to clean URLs
def nettoyer_urls(texte):
    texte = re.sub(r'http[s]?://\S+', ' @url ', texte)
    texte = re.sub(r'www\.\S+', ' @url ', texte)
    texte = re.sub(r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?\b', ' @url ', texte)
    texte = re.sub(r'<\S+>', ' @url ', texte)
    return texte.strip()

# Function to replace IP addresses
def remplacer_adresse_ip(message):
    modele_adresse_ip = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    message = re.sub(modele_adresse_ip, ' @AdIp ', message)
    return message

# Function to replace circuit IDs
def replace_circuit_id(circuit_id):
    patterns = [
        (r'icol\d+', ' icol'),
        (r'icoh\d+', ' icoh'),
        (r'icot\d+', ' icot')
    ]
    for pattern, replacement in patterns:
        circuit_id = re.sub(pattern, replacement, circuit_id)
    return circuit_id

# Function to remove punctuation
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    text = re.sub(r'\d+', '', text)
    return text

# Function to replace abbreviations
def replace_abv(message, df):
    for index, item in df.iterrows():
        abv = item.abreviation
        full_term = item.form_cmplt
        abv_with_spaces = f" {abv}"
        full_term_with_spaces = f" {full_term} "
        message = message.replace(abv_with_spaces, full_term_with_spaces)
    return message

# Lemmatization function
def lemmatize_text(text, lang):
    if lang == 'ang':
        doc = nlp_en(text)
    elif lang == 'fr':
        doc = nlp_fr(text)
    else:
        return text
    return " ".join([token.lemma_ for token in doc])

# Function to remove stop words
def remove_stop_words(text, lang):
    stop_words = set(stopwords.words('english')).union(set(stopwords.words('french')))
    stop_words.update(['bonjour', 'merci', 'être', 'avoir', 'hello', 'hi', 'cher', ' ', 'e'])
    return ' '.join([word for word in text.split() if word not in stop_words])

# Main preprocessing function
def preprocess_message(message, lang):
    message = message.lower()
    message, _ = capturer_texte_avant_delimiteur(message, r'\b(cordialement|salutations|regards|cdt|thanks)\b')
    message = nettoyer_images(message)
    message = replace_Ping_Stats(message)
    message = replace_emails(message)
    message = nettoyer_urls(message)
    message = remplacer_adresse_ip(message)
    message = replace_circuit_id(message) 
    message = remove_punctuation(message)
    message = replace_abv(message, abv_tech)
    message = replace_abv(message, abv_arb)
    message = replace_abv(message, abv_lng)
    message = lemmatize_text(message, lang)
    message = remove_stop_words(message, lang)
    return message
