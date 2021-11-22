SELECT 
	fd.day_of_week,
	w.weekday,
	fd.flight_num,
	fd.origin_airport_id,
	oa.airport_code AS origin_airport_code,
	oa.city_name AS origin_city_name,
	fd.dest_airport_id,
	da.airport_code AS dest_airport_code,
	da.city_name AS dest_city_name,
FROM flight_delays fd
LEFT JOIN airports oa on oa.airport_id = fd.origin_airport_id
LEFT JOIN airports da on da.airport_id = fd.dest_airport_id
LEFT JOIN weekdays w on w.code = fd.day_of_week