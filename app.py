from flask import Flask,request,jsonify,render_template
import config
from Project.utils import MedicalInsurance
import numpy as np
# from flask import jsonify

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('input.html')


@app.route('/input', methods=["POST", "GET"])
def get_insurance():
    if request.method == "POST":
        data = request.form
        age = int(data["age"])
        bmi = float(data["bmi"])
        children = int(data["children"])
        Claim_Amount = float(data["Claim_Amount"])
        past_consultations = float(data["past_consultations"])
        Hospital_expenditure = float(data["Hospital_expenditure"])
        NUmber_of_past_hospitalizations = float(data["NUmber_of_past_hospitalizations"])
        Anual_Salary = float(data["Anual_Salary"])
        sex = data["sex"]
        smoker = data["smoker"]
        region = data["region"]

        med_obj = MedicalInsurance(age, bmi, children, Claim_Amount, past_consultations, 
                                   Hospital_expenditure, NUmber_of_past_hospitalizations, 
                                   Anual_Salary, sex, smoker, region)
        charges = med_obj.get_predict_charges()
        print(charges)

        return render_template('output.html', health_insurance_price=charges)
    
if __name__ == "__main__":
    app.run(debug = True)