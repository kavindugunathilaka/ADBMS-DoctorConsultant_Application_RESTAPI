from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from utils.dbconn import connection
from predict_model.disease_list import DISEASE_LIST

import numpy as np 
import pandas as pd


class PredictResource(Resource):

    def post(self):
        
        if connection is None: return {'message' : 'No Connection'}, HTTPStatus.SERVICE_UNAVAILABLE
        model = pickle.load(open("model.pkl", 'rb'))

        data = request.get_json()
        symptoms = [ data[sym] for sym in data ]

        symptom_record = np.zeros(len(DISEASE_LIST))
        for symptom in symptoms:
            if symptom in DISEASE_LIST:
                ind = DISEASE_LIST.index(symptom)
                symptom_record[ind] = 1
        symptom_record = [list(symptom_record)]
        data_record = pd.DataFrame(list(symptom_record), columns=DISEASE_LIST)
        predicted_disease = model.predict(data_record)

        if len(predicted_disease) == 0: return {"disease" : None}, HTTPStatus.OK

        return { "disease": predicted_disease }