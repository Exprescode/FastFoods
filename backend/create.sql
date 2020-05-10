\c postgres

drop database IF EXISTS cs2102_26;
create database cs2102_26;

\c cs2102_26

create table Areas (
	Name varchar PRIMARY KEY
);

create table Restaurants (
	Id SERIAL PRIMARY KEY,
	Name varchar NOT NULL UNIQUE,
	Type varchar NOT NULL,
	Address varchar NOT NULL,
	Location varchar NOT NULL,
	Area varchar NOT NULL REFERENCES Areas(Name),
	OpenHour TIME(0) NOT NULL,
	CloseHour TIME(0) NOT NULL,
	OrderMin float NOT NULL
);

create table FoodItems (
	Id SERIAL PRIMARY KEY,
	Price float NOT NULL,
	Name varchar NOT NULL,
	Description varchar NOT NULL,
	RestId int NOT NULL REFERENCES Restaurants(Id) ON DELETE CASCADE,
	OrderLimit int NOT NULL,
	CurrentOrders int NOT NULL default 0,
	Category varchar NOT NULL,
	Availability boolean NOT NULL
);

create table Customers (
	Id SERIAL PRIMARY KEY,
	Email varchar NOT NULL unique,
	Password varchar NOT NULL,
	Name varchar NOT NULL,
	Phone int NOT NULL,
	CreditCard bigint NOT NULL,
	Points int NOT NULL DEFAULT 0,
	RegisterDate timestamp NOT NULL default now()
);

create table DeliveryFees (
	Origin varchar NOT NULL REFERENCES Areas(Name),
	Destination varchar NOT NULL REFERENCES Areas(Name),
	Fee float NOT NULL,
	primary key(Origin, Destination)
);

create table Reviews (
	Id SERIAL PRIMARY KEY,
	Rating int NOT NULL,
	Description varchar NOT NULL,
	DateTime timestamp NOT NULL default now()
);

create table Riders (
	Id SERIAL PRIMARY KEY,
	Name varchar NOT NULL,
	Password varchar NOT NULL,
	Email varchar NOT NULL unique,
	Salary float, 
	EmploymentType varchar NOT NULL
);

-- Status: error, ordered, torest, atrest, tocust, completed
create Table Orders (
	Id SERIAL PRIMARY KEY,
	RestId int REFERENCES Restaurants (Id) ON DELETE SET NULL,
	CustId int NOT NULL REFERENCES Customers (Id),
	RiderId int REFERENCES Riders (Id) ON DELETE SET NULL default NULL,
	ReviewId int REFERENCES Reviews (id) default NULL,
	Address varchar NOT NULL,
	Area varchar NOT NULL REFERENCES Areas (Name),
	DeliveryFee float not NULL,
	SubTotal float NOT NULL,
	Total float not NULL,
	PointsUsed float NOT NULL,
	Status varchar NOT NULL default 'error',
	PayMethod varchar NOT NULL,
	OrderTime timestamp NOT NULL default now(),
	ToRestTime timestamp default NULL,
	AtRestTime timestamp default NULL,
	ToCustTime timestamp default NULL,
	AtCustTime timestamp default NULL
);

create table OrderItems (
	OrderId SERIAL NOT NULL,
	UnitPrice float NOT NULL,
	Name varchar NOT NULL,
	Qty int NOT NULL,
	PRIMARY KEY(OrderId, Name),
	FOREIGN KEY (OrderId) REFERENCES Orders (Id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

create table Schedule (
	Id SERIAL PRIMARY KEY,
	RiderId int NOT NULL REFERENCES Riders(Id) ON DELETE CASCADE,
	StartDate date NOT NULL,
	EndDate date NOT NULL,
	Commission float NOT NULL default 0
);

create table Intervals (
	Day int NOT NULL,
	StartHour int NOT NULL,
	EndHour int NOT NULL,
	ScheduleId int NOT NULL references Schedule(Id) ON DELETE CASCADE,
	PRIMARY KEY(ScheduleId, Day, StartHour)
);

create table FdsStaff (
	Id SERIAL PRIMARY KEY,
	Name varchar NOT NULL,
	Password varchar NOT NULL,
	Email varchar NOT NULL unique
);

create table AppPromotions (
	Id SERIAL PRIMARY KEY,
	Code varchar NOT NULL unique DEFAULT 'A' || md5(currval(pg_get_serial_sequence('AppPromotions', 'id'))::varchar),
	DiscountType varchar NOT NULL,
	Discount float NOT NULL,
	MinLimit float NOT NULL DEFAULT 0,
	MaxLimit float NOT NULL DEFAULT 0,
	StartDateTime timestamp NOT NULL,
	EndDateTime timestamp NOT NULL,
	Name varchar NOT NULL,
	Description varchar NOT NULL,
	Condition varchar NOT NULL,
	StaffId SERIAL REFERENCES FdsStaff(id) ON DELETE SET NULL
);

create table RestaurantPromotions (
	Id SERIAL PRIMARY KEY,
	Code varchar NOT NULL unique DEFAULT 'R' || md5(currval(pg_get_serial_sequence('RestaurantPromotions', 'id'))::varchar),
	DiscountType varchar NOT NULL,
	Discount float NOT NULL,
	MinLimit float NOT NULL DEFAULT 0,
	MaxLimit float NOT NULL DEFAULT 0,
	StartDateTime timestamp NOT NULL,
	EndDateTime timestamp NOT NULL,
	Name varchar NOT NULL,
	Description varchar NOT NULL,
	RestId SERIAL NOT NULL REFERENCES Restaurants(Id) ON DELETE CASCADE
);

create table RestaurantPromotionItems (
	PromoId SERIAL NOT NULL REFERENCES RestaurantPromotions(Id)  ON UPDATE CASCADE ON DELETE CASCADE,
	ItemId SERIAL NOT NULL REFERENCES FoodItems(Id) ON UPDATE CASCADE ON DELETE CASCADE,
	Quantity int NOT NULL Default 1,
	PRIMARY KEY(PromoId, ItemId)
);

create table RestaurantStaff (
	Id SERIAL PRIMARY KEY,
	Name varchar NOT NULL,
	Password varchar NOT NULL,
	Email varchar NOT NULL unique,
	RestId int REFERENCES Restaurants(Id) ON DELETE CASCADE
);