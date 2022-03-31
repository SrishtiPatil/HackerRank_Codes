from skense import app
import sys
from flask import request, jsonify
from flask_restful import Resource, Api
from codes.create_json_from_df import Json_from_df
import pickle
import pandas as pd
import spacy
import classy_classification
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
api = Api(app)

@app.route("/", methods=["POST"])

class text_classification(Resource):
 
    def post(self):
        model_ip = request.form.get("model", None)
        file = request.files.get("doc")
        df = pd.read_csv(file)
        pickle_in = open('nlp.p', 'rb')
        saved_m = pickle.load(pickle_in)

        if not file:
            return jsonify({"msg":"file not found", "status":"Failure"}, 400)
     
        if not model_ip:
            return jsonify({"msg":"model not found", "status":"Failure"}, 400)
     
        j = Json_from_df(data_df = df, save_file=False)
        data_df = j.create_json_from_df(data_df = df, save_file=False)
        response = saved_m(data_df["Medical"][6])._.cats
        return jsonify(response)
     
api.add_resource(text_classification, '/skense/text_Classification', endpoint='text_Classification')