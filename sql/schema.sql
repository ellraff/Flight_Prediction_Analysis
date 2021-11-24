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
	origin_airport_id INT,
	dest_airport_id INT,
	dep_time INT,
	arr_time INT,
	arr_delay_group INT
	);
	

SELECT * FROM weekdays



SELECT 
	fd.day_of_week,
	w.weekday,
	fd.origin_airport_id,
	oa.airport_code as origin_airport,
	fd.dest_airport_id,
	da.airport_code as dest_airport,
	fd.dep_time,
	fd.arr_time,
	fd.arr_delay_group
INTO TABLE joined_flight_data2
FROM flight_delays fd
LEFT JOIN airports oa ON oa.airport_id = fd.origin_airport_id
LEFT JOIN airports da ON da.airport_id = fd.dest_airport_id
LEFT JOIN weekdays w ON fd.day_of_week = w.code