import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sqlalchemy import create_engine
import psycopg2
from config import aws_psw
import time

def predictions(day, de_air_id, ar_air_id, dept_time, arr_time):
    db_string = f"postgresql://postgres:{aws_psw}@capstone.c9x4gosspizq.us-east-2.rds.amazonaws.com:5432/Flight_delays"
    engine = create_engine(db_string)
    delays_df = pd.read_sql('''SELECT * FROM flight_delays''', engine)
    
    y = delays_df['arr_delay_group']
    X = delays_df.drop(columns = 'arr_delay_group')

    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    random_state=1)
    scaler = StandardScaler()
    X_scaler = scaler.fit(X_train)

    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    start = time.time()
    rfc = RandomForestClassifier(n_estimators=128, random_state=1)
    rfc.fit(X_train_scaled, y_train)

    return rfc.predict([[day, de_air_id, ar_air_id, dept_time, arr_time]])