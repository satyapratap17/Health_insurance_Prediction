import pickle
import json
import numpy as np
import config

class MedicalInsurance():
    def __init__(self, age, bmi, children, Claim_Amount, past_consultations, Hospital_expenditure, 
                 NUmber_of_past_hospitalizations, Anual_Salary, sex, smoker, region):
        self.age = age
        self.bmi = bmi
        self.children = children
        self.Claim_Amount = Claim_Amount
        self.past_consultations = past_consultations
        self.Hospital_expenditure = Hospital_expenditure
        self.NUmber_of_past_hospitalizations = NUmber_of_past_hospitalizations
        self.Anual_Salary = Anual_Salary
        self.sex = sex.lower()
        self.smoker = smoker.lower()
        self.region = region.lower()

    def load_model(self):
        # we are reading model and json file"
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file)
        with open(config.JOSN_FILE_PATH,"r") as file:
            self.json_data = json.load(file)

    def get_predict_charges(self):
        self.load_model()  # Load the model and JSON data
        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.age
        test_array[1] = self.bmi
        test_array[2] = self.children
        test_array[3] = self.Claim_Amount
        test_array[4] = self.past_consultations
        test_array[5] = self.Hospital_expenditure
        test_array[6] = self.NUmber_of_past_hospitalizations
        test_array[7] = self.Anual_Salary
        test_array[8] = self.json_data["sex"][self.sex]
        test_array[9] = self.json_data["smoker"][self.smoker]
        test_array[10] = self.json_data["region"][self.region]

        predict_charges = self.model.predict([test_array])
        return predict_charges[0]


    




