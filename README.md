# Flight Prediction Analysis

## Overview
I am building a predtion model using data from nationwide flights othroughout the past year.  The goal is to be able to predict whether a flight will be delayed.  This data comes from the Buraeu of Transportation Statistiucs website and allows a user to download a csv with a selection of columns to choose from.  The columns I chose to use as part of my analysis will be shown in the schema below.


## Database
The schema for the database I built uses one table as shown below.

| flight_delays table |
|:-------------------:|
|	year INT
|	month INT         
|	day_of_month INT
|	flight_num INT
|	origin_airport_id INT
|	origin_airport_code VARCHAR(3)
|	origin_city_name VARCHAR
|	origin_state_nm VARCHAR
|	dest_airport_id INT
| dest_airport_code VARCHAR (3)
|	dest_city_name VARCHAR
|	dest_state_nm VARCHAR
|	dept_time INT
|	arr_time INT
|	arr_delay FLOAT
|	cancelled FLOAT
|	air_time FLOAT
|	flights FLOAT
|	distance FLOAT
| carrier_delay FLOAT
|	weather_delay FLOAT
|	NAS_delay FLOAT
|	security_delay FLOAT
|	late_aircraft_delay FLOAT

## Model

Using the database above, I remove the varchar columns and transform the delay minutes column by using delays over 15 minutes as 1, or delayed and delays under 15 minutes as 0 or not delayed.  I use 15 minutes because that's usually well within acceptable for an arrival flight delay.  More then that can cause people to miss connecting flights.  The rest of the parameters will be used to train the data including where the flight took off, how long the flight is, where the destination is and so forth.  I plan to use data from the past year but even this sample dataset, which is only august 2021 is 570,000 rows so the dataset will be large.  For this reason I have chosen to use the Random Forest model because there are many classifier so the extra branches will be helpful and protect against over sampling.  Also, since the dataset is so large, the Random Forest Classifier willmanage the large dataset better then the others.
