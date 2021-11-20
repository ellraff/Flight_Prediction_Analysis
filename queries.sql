CREATE TABLE flight_delays (
	year INT,
	month INT,
	day_of_month INT,
	flight_num INT,
	origin_airport_id INT,
	origin_airport_code VARCHAR(3),
	origin_city_name VARCHAR,
	origin_state_nm VARCHAR,
	dest_airport_id INT,
	dest_airport_code VARCHAR (3),
	dest_city_name VARCHAR,
	dest_state_nm VARCHAR,
	dept_time INT,
	arr_time INT,
	arr_delay FLOAT,
	cancelled FLOAT,
	air_time FLOAT,
	flights FLOAT,
	distance FLOAT,
	carrier_delay FLOAT,
	weather_delay FLOAT,
	NAS_delay FLOAT,
	security_delay FLOAT,
	late_aircraft_delay FLOAT
	);
	