-- "<path>\pg_dump.exe" --column-inserts --data-only --table=<table_name> cs2102_26

-- password = qwerty
insert into customers (email, password, name, phone, creditcard) values ('test@test.com', '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5', 'qwerty', 12345678, 1234567890123456);
insert into customers (email, password, name, phone, creditcard) values ('test1@test.com', '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5', 'qwerty', 12345678, 1234567890123456);

insert into Areas (name) values ('North');
insert into Areas (name) values ('South');
insert into Areas (name) values ('East');
insert into Areas (name) values ('West');
insert into Areas (name) values ('Central');

insert into deliveryfees (origin, destination, fee) values ('North', 'North', 3);
insert into deliveryfees (origin, destination, fee) values ('North', 'South', 7);
insert into deliveryfees (origin, destination, fee) values ('North', 'East', 5);
insert into deliveryfees (origin, destination, fee) values ('North', 'West', 5);
insert into deliveryfees (origin, destination, fee) values ('North', 'Central', 5);
insert into deliveryfees (origin, destination, fee) values ('South', 'North', 7);
insert into deliveryfees (origin, destination, fee) values ('South', 'South', 3);
insert into deliveryfees (origin, destination, fee) values ('South', 'East', 5);
insert into deliveryfees (origin, destination, fee) values ('South', 'West', 5);
insert into deliveryfees (origin, destination, fee) values ('South', 'Central', 5);
insert into deliveryfees (origin, destination, fee) values ('East', 'North', 5);
insert into deliveryfees (origin, destination, fee) values ('East', 'South', 5);
insert into deliveryfees (origin, destination, fee) values ('East', 'East', 3);
insert into deliveryfees (origin, destination, fee) values ('East', 'West', 7);
insert into deliveryfees (origin, destination, fee) values ('East', 'Central', 5);
insert into deliveryfees (origin, destination, fee) values ('West', 'North', 5);
insert into deliveryfees (origin, destination, fee) values ('West', 'South', 5);
insert into deliveryfees (origin, destination, fee) values ('West', 'East', 7);
insert into deliveryfees (origin, destination, fee) values ('West', 'West', 3);
insert into deliveryfees (origin, destination, fee) values ('West', 'Central', 5);
insert into deliveryfees (origin, destination, fee) values ('Central', 'North', 5);
insert into deliveryfees (origin, destination, fee) values ('Central', 'South', 5);
insert into deliveryfees (origin, destination, fee) values ('Central', 'East', 5);
insert into deliveryfees (origin, destination, fee) values ('Central', 'West', 5);
insert into deliveryfees (origin, destination, fee) values ('Central', 'Central', 3);

insert into Restaurants (name, type, address, location, area, openhour, closehour, ordermin) values
('A-One Claypot House', 'Chinese', 'Jurong Point, 1 Jurong West Central 2 #03-09, 648886 Singapore', 'Jurong Point', 'West', '10:30', '21:30', 1),
('4Fingers', 'Western', '68 Orchard Rd, #B1-07 Singapore 238839', 'Plaza Singapura', 'Central', '11:00', '21:30', 1),
('MakiSan', 'Japanese', '8 Grange Road #B1-06, Cineleisure Orchard, Singapore, 239695', 'Cineleisure', 'Central', '11:30', '21:00', 1);

insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (13.8, 'Gong Bao Chicken Set', 'Serves with rice, braised peanuts and seasonal vegetable', 1, 50, 0, 'Rice', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (12.73, 'Dried Scallop Porridge with Century Egg & Minced Meat', 'Dried scallops with century egg and minced meat, choice of add-on available (Dried scallops cannot be removed from the porridge)', 1, 50, 0, 'Congee', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (12.73, 'Premium Dried Scallop Porridge', 'White rice as base with dried scallops, fish slices and cuttlefish, choice of add-on available (Dried scallops cannot be removed from the porridge)', 1, 50, 0, 'Congee', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (13.8, 'Claypot Chicken and Mushroom Rice', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 1, 50, 0, 'Rice', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (15.94, 'Shrimps Fried Rice with XO Sauce', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 1, 50, 0, 'Rice', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (13.8, 'Claypot Seafood Noodle', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 1, 50, 0, 'Noodle', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (13.8, 'Gong Bao Chicken Noodle', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 1, 50, 0, 'Noodle', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (15.94, 'Crab Meat Seafood Fried Rice', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 1, 50, 0, 'Rice', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (13.8, 'Beancurd with Seafood and Minced Meat Set', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 1, 50, 0, 'Rice', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (13.8, 'Honey Sweet & Sour Pork Set', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 1, 50, 0, 'Rice', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (12.35, 'Wingettes and Drumettes Combo', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 2, 30, 0, 'Set', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (9.5, 'Wingettes and Drumettes A La Carte', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 2, 30, 0, 'A La Carte', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (12.3, 'Chicken Drumsticks Combo', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 2, 30, 0, 'Set', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (9.5, 'Chicken Drumsticks A La Carte', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 2, 30, 0, 'A La Carte', TRUE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (10.9, 'California Dreaming', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 3, 0, 0, 'Sushi', FALSE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (11.9, 'Salmon Says', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 3, 0, 0, 'Sushi', FALSE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (8.9, 'Lucky Roll', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 3, 0, 0, 'Sushi', FALSE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (11.9, 'Tom-Yummy', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 3, 0, 0, 'Sushi', FALSE);
insert into FoodItems (price, name, description, restid, orderlimit, currentorders, category, availability) values (13.9, 'Soul-Veggie', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare euismod molestie. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse varius interdum enim vitae laoreet.', 3, 0, 0, 'Sushi', FALSE);

insert into fdsstaff (name, password, email) values ('tester', '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5', 'test@test.com');

insert into AppPromotions (discounttype, discount, minlimit, maxlimit, startdatetime, enddatetime, name, description, condition, staffid) values
('percent', 0.1, 10.0, 0, '2020-01-01 00:00', '2022-01-01 00:00', 'First Order', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'new user', 1),
('flat', 2, 10.0, 0, '2020-01-01 00:00', '2021-01-01 00:00', 'Return Customer', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'return user', 1),
('percent', 0.1, 10.0, 0, '2020-01-01 00:00', '2020-01-02 00:00', 'Next Order', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'new user', 1);

insert into RestaurantPromotions (discounttype, discount, minlimit, maxlimit, startdatetime, enddatetime, name, description, restid) values
('percent', 0.1, 10.0, 0, '2020-01-01 00:00', '2022-01-01 00:00', 'Specials Offer', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 1),
('flat', 1, 10.0, 0, '2020-01-01 00:00', '2021-01-01 00:00', 'First Come First Serve', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 1);

insert into RestaurantPromotionItems (promoid, itemid, quantity) values
(1, 1, 1),
(1, 2, 2),
(1, 3, 3);

INSERT INTO public.orders (id, restid, custid, reviewid, address, area , deliveryfee, subtotal, total, pointsused, status, paymethod, ordertime, toresttime, atresttime, tocusttime, atcusttime) VALUES (1, 1, 1, NULL, 'Block EEE ABC Street 123 #12-123 Singapore 123456', 'Central', 5, 695, 625.99, 1, 'ordered', 'card', '2020-05-01 17:36:00.406558', NULL, NULL, NULL, NULL);
INSERT INTO public.orders (id, restid, custid, reviewid, address, area , deliveryfee, subtotal, total, pointsused, status, paymethod, ordertime, toresttime, atresttime, tocusttime, atcusttime) VALUES (2, 1, 1, NULL, 'Block EEE ABC Street 123 #12-123 Singapore 123456', 'Central', 5, 68.65, 68.65, 0, 'ordered', 'card', '2020-05-01 17:42:34.880485', NULL, NULL, NULL, NULL);

INSERT INTO public.orderitems (orderid, unitprice, name, qty) VALUES (1, 13.8, 'Gong Bao Chicken Set', 50);
INSERT INTO public.orderitems (orderid, unitprice, name, qty) VALUES (2, 12.73, 'Dried Scallop Porridge with Century Egg & Minced Meat', 5);

insert into restaurantstaff (name,password, email,restid) values ('test','65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5','test@test.com', 1);

insert into riders (name, password, email, salary, employmenttype) values ('tester', '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5', 'test@test.com', 1000, 'full');
insert into riders (name, password, email, salary, employmenttype) values ('tester2', '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5', 'test1@test.com', 1000, 'part');
