CREATE TABLE bus
(
	bus_no varchar(10),
	b_date date,
	source varchar(30), 
	destination varchar(30), 
	departure_time time, 
	total_seats int,
	PRIMARY KEY(b_date,bus_no) 
);

CREATE TABLE govt
(
	state varchar(15) PRIMARY KEY, 
	travel_dept varchar(30)
);


CREATE TABLE travel_agency
(
	gst_no varchar(15) PRIMARY KEy,
	agency_name varchar(20), 
	state varchar(15) references govt(state)
);

CREATE TABLE bus_belongsto
(
	bus_no varchar(10),
	b_date date,
	gst_no varchar(15) ,
	PRIMARY KEY(bus_no, b_date, gst_no),
	foreign key(bus_no,b_date) references bus( bus_no,b_date),
	foreign key  (gst_no)  references  travel_agency(gst_no)
);

CREATE TABLE passengers
(
	passenger_id integer PRIMARY KEY , 
	passenger_name text, 
	pickup_point varchar(50), 
	drop_point varchar(50), 

	contact char(10),
	aadhaar_uid varchar(19),

	bus_no varchar(10)	,
	b_date date,
	gst_no varchar(15),
	foreign key( bus_no , b_date , gst_no) references bus_belongsto(bus_no, b_date , gst_no)
);


CREATE TABLE ticket
(
	ticket_id integer PRIMARY KEY , 
	ticket_book_date date,
	date_of_journey date,
	seat_no integer,
	fare integer, 
	passenger_id integer  references  passengers(passenger_id) 
);


CREATE TABLE route
(

	route_id SERIAL PRIMARY KEY , 
	bus_no varchar(10),
	b_date date,
	pickup_point varchar(50), 
	drop_point varchar(50), 
	departure_time time, 

	foreign key( bus_no , b_date ) references bus( bus_no , b_date )
);


