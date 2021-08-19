from flask import Flask
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello'