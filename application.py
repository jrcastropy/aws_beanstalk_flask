from flask import Flask
from flask_restful import Resource, Api
from itertools import chain
import json

import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

application = Flask(__name__)
api = Api(application)

@application.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello'

class SynApi(Resource):

    def get(self, word):

        synonyms = wordnet.synsets(word)
        lemmas = list(chain.from_iterable([word.lemma_names() for word in synonyms]))

        x = json.dumps(lemmas)
        return {"synonyms":x}


api.add_resource(SynApi, '/Syn/<string:word>')

if __name__ == '__main__':
    application.run(debug=True)