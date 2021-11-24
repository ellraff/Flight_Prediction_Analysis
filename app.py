import pandas as pd
from sqlalchemy import create_engine

from flask import Flask, render_template, request
from config import aws_psw
from run_ml import predictions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        weekday = request.form["weekday"].lower()
        dep_code = request.form["depcode"]
        arr_code = request.form["arrcode"]
        dep_time = int(request.form["deptime"])
        arr_time = int(request.form["arrtime"])
        

        db_string = f"postgresql://postgres:{aws_psw}@capstone.c9x4gosspizq.us-east-2.rds.amazonaws.com:5432/Flight_delays"
        engine = create_engine(db_string)

        weekdays_df =  pd.read_sql('''SELECT * FROM weekdays''', engine)
        airports_df =  pd.read_sql('''SELECT * FROM airports''', engine)
        
        weekdays_map = {
            d['weekday'].lower(): d['code']
            for d in weekdays_df.to_dict('records')
            }
        airports_map = {
            d['airport_code']:{
                'airport_id':d['airport_id'],
                'city_name': d['city_name']
                } for d in airports_df.to_dict('records')
        }
        de_air_id = airports_map[dep_code]['airport_id']
        ar_air_id = airports_map[arr_code]['airport_id']
        day = weekdays_map[weekday]
        de_city_name = airports_map[dep_code]['city_name']
        ar_city_name = airports_map[arr_code]['city_name']


        if dep_time < 800:
            dep_group = 1
        elif dep_time < 1100:
            dep_group = 2
        elif dep_time < 1400:
            dep_group = 3
        elif dep_time < 1700:
            dep_group = 4
        elif dep_time < 2000:
            dep_group = 5
        else:
            dep_group = 6
            
        if arr_time< 800:
            arr_group = 1
        elif arr_time< 1100:
            arr_group = 2
        elif arr_time< 1400:
            arr_group = 3
        elif arr_time< 1700:
            arr_group = 4
        elif arr_time< 2000:
            arr_group = 5
        else:
            arr_group = 6

        prediction = predictions(day, de_air_id, ar_air_id, dep_group, arr_group)

        output = prediction[0]


        if(output == 0):
            results = (f'The flight from {de_city_name} to {ar_city_name} should be on time and may even have an early arrival!')
        elif(output == 1):
            results = (f"The flight from {de_city_name} to {ar_city_name} may be delayed up to 15 minutes which hopefully won't set you back to much, but if you have a short layover, I'd try to increase it")
        elif(output == 2):
            results = (f'The flight from {de_city_name} to {ar_city_name} may be delayed more then 30 minutes.  If you have a connecting flight, you may paln to have a connecting flight, you may want to ensure you have at least an hour layover, or take an earlier flight!')


        return render_template("results.html", results=results)


        