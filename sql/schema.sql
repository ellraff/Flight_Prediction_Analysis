DROP TABLE flight_delays;
DROP TABLE weekdays;
DROP TABLE airports;

CREATE TABLE airports (
	airport_id INT,
	airport_code VARCHAR(3),
	city_name VARCHAR
	);
	
CREATE TABLE weekdays (
	code INT,
	weekday TEXT
	);
	
CREATE TABLE flight_delays (
	day_of_week INT,
	flight_num INT,
	origin_airport_id INT,
	dest_airport_id INT,
	dept_time INT,
	arr_time INT,
	arr_del15 FLOAT,
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
	

SELECT * FROM weekdays