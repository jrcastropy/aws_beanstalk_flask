from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from itertools import chain
import json

import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

application = Flask(__name__)
api         = Api(application)

@application.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello'

class SynApi(Resource):

    def post(self):
        payl        = request.get_json()
        data_list   = payl['data']

        res_dict    = {}

        for word in data_list:
            synonyms        = wordnet.synsets(word)
            lemmas          = list(dict.fromkeys(chain.from_iterable([word.lemma_names() for word in synonyms])))
            result_synonyms = json.dumps(lemmas)
            res_dict[word]  = result_synonyms

        return jsonify(res_dict)

api.add_resource(SynApi, '/Syn')

if __name__ == '__main__':
    application.run(debug=True)