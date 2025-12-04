from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

def get_clean_data(form_data):
    gestation = float(form_data['gestation'])
    parity = int(form_data['parity'])
    age = int(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = float(form_data['smoke'])

    cleaned_data = {
        'gestation': [gestation],
        'parity': [parity],
        'age': [age],
        'height': [height],
        'weight': [weight],
        'smoke': [smoke]
    }

    return cleaned_data

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    # Get and clean user input
    baby_data_form = request.form
    baby_data_cleaned = get_clean_data(baby_data_form)

    # Convert into dataframe
    baby_df = pd.DataFrame(baby_data_cleaned)

    # Load trained model
    with open('model/model.pkl', 'rb') as obj:
        mymodel = pickle.load(obj)

    # Make prediction
    prediction = mymodel.predict(baby_df)
    prediction = round(float(prediction[0]), 2)

    # Return JSON response
    response = {'prediction': prediction}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
