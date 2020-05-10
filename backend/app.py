#!/usr/bin/python3
import flask
import psycopg2
import hashlib
import ast
import threading
import time
import datetime as dt
import re

from flask_cors import CORS
from psycopg2 import errors
from flask import request, jsonify
from datetime import datetime, timedelta
from pytz import timezone
import calendar


try:
  connection = psycopg2.connect(user = "postgres",
                                password = "postgres",
                                host = "127.0.0.1",
                                port = "5432",
                                database = "cs2102_26")
  cursor = connection.cursor()
except (Exception, psycopg2.Error) as error :
	print ("Error while connecting to PostgreSQL", error)


app = flask.Flask(__name__)
CORS(app)
# if CORS(app) does not work.
# CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/v1/fdsstaff/getlist', methods=['GET'])
def get_fdsstaff_list():
	selectStatement = "select id, name, email from fdsstaff order by name;"
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/fdsstaff/getuser', methods=['POST'])
def get_fdsstaff_user():
	args = request.json
	email = args['email']
	password = hashlib.sha256(args['password'].encode()).hexdigest()
	selectStatement = "select id, email, name from fdsstaff where email='%s' and password='%s';" % (email, password)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchone()
	if r:
		return jsonify(r)
	else:
		return "fail"

@app.route('/api/v1/fdsstaff/addstaff', methods=['POST'])
def add_fdsstaff():
	args = request.json

	name = args['name']
	email = args['email']
	pwd = args['password']

	if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
		return 'Invalid email address!'

	if len(pwd) < 6:
		return 'Password too short!'

	pwd = hashlib.sha256(pwd.encode()).hexdigest()

	try:
		insertStatement = "insert into fdsstaff (name, password, email) values ('%s', '%s', '%s');" % (name, pwd, email)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Email already exist!'

	return 'pass'

@app.route('/api/v1/fdsstaff/updatestaff', methods=['POST'])
def update_fdsstaff():
	args = request.json

	sid = args['id']
	name = args['name']
	email = args['email']

	if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
		return 'Invalid email address!'

	pwd = ''
	if 'password' in args:
		pwd = args['password']
		if len(pwd) < 6:
			return 'Password too short!'
		pwd = hashlib.sha256(pwd.encode()).hexdigest()
		statement = "update fdsstaff set name='%s', password='%s', email='%s' where id=%s returning id;" % (name, pwd, email, sid)
	else:
		statement = "update fdsstaff set name='%s', email='%s' where id=%s returning id;" % (name, email, sid)

	try:
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Email already exist!'

	if cursor.fetchone():
		return 'pass'

@app.route('/api/v1/fdsstaff/deletestaff', methods=['POST'])
def delete_fdsstaff():
	args = request.json

	sid = args['id']

	try:
		statement = "delete from fdsstaff where id=%s;" % (sid)
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	return 'pass'

@app.route('/api/v1/riders/getsummary', methods=['GET'])
def get_riders_summary():
	selectStatement = "select id, name, email, salary, employmenttype, (select coalesce(sum(date_part('hour', atcusttime - toresttime)*60 + date_part('minute', atcusttime - toresttime))/count(*),0) from orders where riderid=r1.id and atcusttime is not null), (select count(reviewid) from orders where riderid=r1.id), (select coalesce(sum(r2.rating)/count(r2.id), 0) from orders o1 left join reviews r2 on o1.reviewid=r2.id where o1.riderid=r1.id) from riders r1 order by name;"
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/riders/getuser', methods=['POST'])
def get_riders_user():
	args = request.json
	email = args['email']
	password = hashlib.sha256(args['password'].encode()).hexdigest()
	selectStatement = "select id, email, name, salary, employmenttype from riders where email='%s' and password='%s';" % (email, password)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchone()
	if r:
		return jsonify(r)
	else:
		return "fail"

@app.route('/api/v1/riders/updatepassword', methods=['POST'])
def update_riders_password():
	args = request.json

	rid = args['id']
	opwd = args['opwd']
	npwd = args['npwd']

	if len(opwd) < 6 or len(npwd) < 6:
		return 'Password too short!'

	opwd = hashlib.sha256(opwd.encode()).hexdigest()
	npwd = hashlib.sha256(npwd.encode()).hexdigest()

	try:
		insertStatement = "update riders set password='%s' where id=%s and password='%s' returning id;" % (npwd, rid, opwd)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	if cursor.fetchone():
		return 'pass'
		
	return 'Current password does not match!'

@app.route('/api/v1/riders/addrider', methods=['POST'])
def add_rider():
	args = request.json

	name = args['name']
	email = args['email']
	salary = args['salary']
	employmentType = args['type']
	pwd = args['password']

	if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
		return 'Invalid email address!'

	if len(pwd) < 6:
		return 'Password too short!'

	pwd = hashlib.sha256(pwd.encode()).hexdigest()

	try:
		insertStatement = "insert into riders (name, password, email, salary, employmenttype) values ('%s', '%s', '%s', %s, '%s');" % (name, pwd, email, salary, employmentType)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Email already exist!'

	return 'pass'

@app.route('/api/v1/riders/updateRider', methods=['POST'])
def update_rider():
	args = request.json

	rid = args['id']
	name = args['name']
	email = args['email']
	salary = args['salary']
	employmentType = args['type']

	if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
		return 'Invalid email address!'

	pwd = ''
	if 'password' in args:
		pwd = args['password']
		if len(pwd) < 6:
			return 'Password too short!'
		pwd = hashlib.sha256(pwd.encode()).hexdigest()
		statement = "update riders set name='%s', password='%s', email='%s', salary=%s, employmenttype='%s' where id=%s returning id;" % (name, pwd, email, salary, employmentType, rid)
	else:
		statement = "update riders set name='%s', email='%s', salary=%s, employmenttype='%s' where id=%s returning id;" % (name, email, salary, employmentType, rid)

	try:
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Email already exist!'

	if cursor.fetchone():
		return 'pass'

@app.route('/api/v1/riders/deleteRider', methods=['POST'])
def delete_rider():
	args = request.json

	rid = args['id']

	try:
		statement = "delete from riders where id=%s;" % (rid)
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	return 'pass'

@app.route('/api/v1/customers/getcustomer', methods=['POST'])
def get_customer():
	args = request.json
	email = args['email']
	password = hashlib.sha256(args['password'].encode()).hexdigest()
	selectStatement = "select id, email, name, phone, creditcard, points from customers where email='%s' and password='%s';" % (email, password)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchone()
	if r:
		return jsonify(r)
	else:
		return "fail"

@app.route('/api/v1/customers/addcustomer', methods=['POST'])
def add_customer():
	regex = r'[^@]+@[^@]+\.[^@]+'
	args = request.json

	email = args['email']
	password = args['password']
	name = args['name']
	phone = args['phone']
	card = args['card']

	if not re.match(regex,email):
		return 'Invalid email address!'
	if(len(password) < 6):
		return 'Password too short!'
	if(len(name) < 6):
		return 'Name too short!'
	if(len(phone) != 8 or not phone.isnumeric()):
		return 'Invalid phone number!'
	if(len(card) != 16 or not card.isnumeric()):
		return 'Invalid credit card number!'
	
	password = hashlib.sha256(password.encode()).hexdigest()

	try:
		insertStatement = "insert into customers (email,password,name,phone,creditcard) values ('%s','%s','%s',%s, %s);" % (email, password, name, phone, card)
		print(insertStatement)
		cursor.execute(insertStatement)
		connection.commit()
	# except errors.UniqueViolation as e:
	# 	return 'Email address already in use!'
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/customers/updatecustomer', methods=['POST'])
def update_customer():
	regex = r'[^@]+@[^@]+\.[^@]+'
	args = request.json

	email = args['email']
	name = args['name']
	password = args['password']
	phone = args['phone']
	card = args['card']
	tableId = args['tableId']

	if not re.match(regex,email):
		return 'Invalid email address!'
	if(len(name) < 6):
		return 'Name too short!'
	if(len(password) > 0 and len(password) < 6):
		return 'Password too short!'
	if(len(phone) != 8 or not phone.isnumeric()):
		return 'Invalid phone number!'
	if(len(card) != 16 or not card.isnumeric()):
		return 'Invalid credit card number!'

	try:
		if(len(password) > 0):
			password = hashlib.sha256(password.encode()).hexdigest()
			insertStatement = "update customers set email='%s', password='%s', name='%s', phone=%s, creditcard=%s where id=%s;" % (email, password, name, phone, card, tableId)
		else:
			insertStatement = "update customers set email='%s', name='%s', phone=%s, creditcard=%s where id=%s;" % (email, name, phone, card, tableId)
		cursor.execute(insertStatement)
		connection.commit()
	except UniqueViolation as e:
		return 'Email address already in use!'
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/restaurantstaff/getlist', methods=['GET'])
def get_restaurantstaff_list():
	rid = request.args.get('id')
	selectStatement = "select id, name, email from restaurantstaff where restid=%s order by name;" % (rid)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	if not r:
		r = ()
	return jsonify(r)

@app.route('/api/v1/restaurantstaff/getuser', methods=['POST'])
def get_restaurantstaff_user():
	args = request.json
	email = args['email']
	password = hashlib.sha256(args['password'].encode()).hexdigest()
	selectStatement = "select id, email, name, restid from RestaurantStaff where email='%s' and password='%s';" % (email, password)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchone()
	if r:
		return jsonify(r)
	else:
		return "fail"

@app.route('/api/v1/restaurantstaff/updatepassword', methods=['POST'])
def update_restaurantstaff_password():
	args = request.json

	uid = args['uid']
	opwd = args['opwd']
	npwd = args['npwd']

	if len(opwd) < 6 or len(npwd) < 6:
		return 'Password too short!'

	opwd = hashlib.sha256(opwd.encode()).hexdigest()
	npwd = hashlib.sha256(npwd.encode()).hexdigest()

	try:
		insertStatement = "update restaurantstaff set password='%s' where id=%s and password='%s' returning id;" % (npwd, uid, opwd)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	if cursor.fetchone():
		return 'pass'
		
	return 'Current password does not match!'

@app.route('/api/v1/restaurantstaff/addstaff', methods=['POST'])
def add_restaurantstaff():
	args = request.json

	rid = args['rid']
	name = args['name']
	email = args['email']
	pwd = args['password']

	if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
		return 'Invalid email address!'

	if len(pwd) < 6:
		return 'Password too short!'

	pwd = hashlib.sha256(pwd.encode()).hexdigest()

	try:
		insertStatement = "insert into RestaurantStaff (name, password, email, restid) values ('%s', '%s', '%s', %s);" % (name, pwd, email, rid)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Email already exist!'

	return 'pass'

@app.route('/api/v1/restaurantstaff/updatestaff', methods=['POST'])
def update_restaurantstaff():
	args = request.json

	sid = args['id']
	name = args['name']
	email = args['email']

	if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
		return 'Invalid email address!'

	pwd = ''
	if 'password' in args:
		pwd = args['password']
		if len(pwd) < 6:
			return 'Password too short!'
		pwd = hashlib.sha256(pwd.encode()).hexdigest()
		statement = "update RestaurantStaff set name='%s', password='%s', email='%s' where id=%s returning id;" % (name, pwd, email, sid)
	else:
		statement = "update RestaurantStaff set name='%s', email='%s' where id=%s returning id;" % (name, email, sid)

	try:
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Email already exist!'

	if cursor.fetchone():
		return 'pass'

@app.route('/api/v1/restaurantstaff/deletestaff', methods=['POST'])
def delete_restaurantstaff():
	args = request.json

	sid = args['id']

	try:
		statement = "delete from RestaurantStaff where id=%s;" % (sid)
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	return 'pass'

@app.route('/api/v1/restaurants/gettype', methods=['GET'])
def get_restaurant_type():
		
	selectStatement = "select distinct r1.type from restaurants r1 left join fooditems f1 on r1.id = f1.restid where availability=true order by r1.type asc;"

	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	
	return jsonify(r)

@app.route('/api/v1/restaurants/getlist', methods=['GET'])
def get_restaurant_list():
	area = request.args.get('area')
	selectStatement = "select r1.id,r1.name,r1.type,r1.location, d1.fee from restaurants r1 left join deliveryfees d1 on r1.area = d1.origin where localtime >= r1.openhour and localtime <= r1.closehour and r1.id in (select restid from fooditems where availability=true) and destination='%s'order by r1.name asc, r1.location asc;" % (area)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/restaurants/getnamelist', methods=['GET'])
def get_restaurant_namelist():
	selectStatement = "select id, name from restaurants order by name asc;"
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/restaurants/getsearch', methods=['GET'])
def get_restaurant_search():
	search = request.args.get('search')
	area = request.args.get('area')
	selectStatement = "select r1.id,r1.name,r1.type,r1.location, d1.fee from restaurants r1 left join deliveryfees d1 on r1.area = d1.origin where r1.name ilike '%{0}%' and r1.id in (select restid from fooditems where availability=true) and destination='{1}' order by r1.name asc, r1.location asc;".format(search,area)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	
	return jsonify(r)

@app.route('/api/v1/restaurants/getfilter', methods=['GET'])
def get_restaurant_filter():
	category = request.args.get('category')
	area = request.args.get('area')
	selectStatement = "select r1.id,r1.name,r1.type,r1.location, d1.fee from restaurants r1 left join deliveryfees d1 on r1.area = d1.origin where r1.type='%s' and r1.id in (select restid from fooditems where availability=true) and destination='%s' order by r1.name asc, r1.location asc;" % (category,area)

	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	
	return jsonify(r)

@app.route('/api/v1/restaurants/getfdslist', methods=['GET'])
def get_restaurant_fdslist():
	selectStatement = "select id, name, type, address, location, area, to_char(openhour, 'HH24:MI'), to_char(closehour, 'HH24:MI'), ordermin, (select count(*) from restaurantstaff where restid=r1.id), (select count(*) from fooditems where restid=r1.id), (select count(reviewid) from orders where restid=r1.id and extract(year from ordertime)=extract(year from now())), (select coalesce(sum(r2.rating)/count(o1.reviewid), 0) from orders o1 left join reviews r2 on o1.reviewid=r2.id where o1.restid=r1.id and extract(year from ordertime)=extract(year from now())) from restaurants r1 order by name;"
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/restaurants/addrestaurant', methods=['POST'])
def add_restaurant():
	args = request.json

	name = args['name']
	restType = args['type']
	addr = args['address']
	location = args['location']
	area = args['area']
	minorder = args['minorder']
	ohour = args['ohour']
	chour = args['chour']

	if ohour > chour:
		return 'Opening hours cannot be come after closing hours.'
	
	try:
		insertStatement = "insert into Restaurants (name, type, address, location, area, openhour, closehour, ordermin) values ('%s', '%s', '%s',' %s', '%s', '%s', '%s', '%s');" % (name, restType, addr, location, area, ohour, chour, minorder)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/restaurants/updaterestaurant', methods=['POST'])
def update_restaurant():
	args = request.json

	rid = args['id']
	name = args['name']
	restType = args['type']
	addr = args['address']
	location = args['location']
	area = args['area']
	minorder = args['minorder']
	ohour = args['ohour']
	chour = args['chour']

	if ohour > chour:
		return 'Opening hours cannot be come after closing hours.'
	
	try:
		insertStatement = "update Restaurants set name='%s', type='%s', address='%s', location='%s', area='%s', openhour='%s', closehour='%s', ordermin='%s' where id=%s returning id;" % (name, restType, addr, location, area, ohour, chour, minorder, rid)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	if not cursor.fetchone():
		return 'Invalid input.'

	return 'pass'

@app.route('/api/v1/restaurants/deleterestaurant', methods=['POST'])
def delete_restaurant():
	args = request.json

	rid = args['id']

	try:
		insertStatement = "delete from restaurants where id=%s;" % (rid)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	return 'pass'

@app.route('/api/v1/areas/getareas', methods=['GET'])
def get_areas():
	selectStatement = "select name from areas;"
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/fooditems/gettype', methods=['GET'])
def get_fooditem_type():
	restId = request.args.get('id')
		
	selectStatement = "select distinct category from fooditems where restid=%s and availability=true order by category asc;" % (restId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/fooditems/getlist', methods=['GET'])
def get_fooditem_list():
	restId = request.args.get('id')
	
	selectStatement = "select id, price, name, description, orderlimit, currentorders, category from fooditems where restid=%s and availability=true order by name;" % (restId)
	cursor.execute(selectStatement)
	connection.commit()
	record = cursor.fetchall()

	return jsonify(record)

@app.route('/api/v1/fooditems/getsearch', methods=['GET'])
def get_fooditem_search():
	search = request.args.get('search')
	restId = request.args.get('id')
	selectStatement = "select id, price, name, description, orderlimit, currentorders, category from fooditems where name ilike '%{0}%' and restid={1} and availability=true order by name;".format(search,restId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	
	return jsonify(r)

@app.route('/api/v1/fooditems/getfilter', methods=['GET'])
def get_fooditem_filter():
	category = request.args.get('category')
	restId = request.args.get('id')
	selectStatement = "select id, price, name, description, orderlimit, currentorders, category from fooditems where category='%s' and restid=%s and availability=true order by name;" % (category,restId)

	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	
	return jsonify(r)

@app.route('/api/v1/fooditems/additem', methods=['POST'])
def add_foodItem():
	args = request.json

	restId = args['id']
	price = args['price']
	limit = args['limit']
	name = args['name']
	descript = args['description']
	category = args['category']
	availability = False

	try:
		float(price)
		availability = (int(limit) > 0)
	except Exception as e:
		return 'Invalid input.'

	try:
		insertStatement = "insert into fooditems (price, name, description, restid, orderlimit, category, availability) values (%s, '%s', '%s', %s, %s, '%s', %s);" % (price, name, descript, restId, limit, category, availability)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/fooditems/updateitem', methods=['POST'])
def update_foodItem():
	args = request.json

	itemId = args['id']
	price = args['price']
	limit = args['limit']
	name = args['name']
	descript = args['description']
	category = args['category']

	try:
		insertStatement = "update fooditems set price=%s, orderlimit=%s, name='%s', description='%s', category='%s' where id=%s;" % (price, limit, name, descript, category, itemId)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/fooditems/deleteitem', methods=['POST'])
def delete_foodItem():
	args = request.json

	itemId = args['id']

	try:
		insertStatement = "delete from fooditems where id=%s;" % (itemId)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/apppromotions/getlist', methods=['GET'])
def get_apppromotion_list():
	selectStatement = "select id, code, discounttype, discount, minlimit, maxlimit, name, description, EXTRACT(DAY FROM enddatetime - now()) + 1 from apppromotions where startdatetime <= now() and enddatetime >= now() order by startdatetime asc;"
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/apppromotions/getfdslist', methods=['GET'])
def get_apppromotion_fdslist():
	selectStatement = "select id, code, discounttype, discount, minlimit, maxlimit, to_char(startdatetime, 'DD-MM-YY'), to_char(enddatetime, 'DD-MM-YY'), name, description, condition from apppromotions order by startdatetime desc;"
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/apppromotions/getentry', methods=['GET'])
def get_apppromotion_entry():
	custid = request.args.get('id')
	code = request.args.get('code')
	selectStatement = "select id, code, discounttype, discount, minlimit, maxlimit, name, description, condition from apppromotions where code='%s' and startdatetime <= now() and enddatetime >= now();" % (code)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchone()
	if not r:
		return "Invalid promotion code."
	if r[-1] == 'new user':
		selectStatement = "select count(*) from orders where custid=%s and status<>'error';" % (custid)
		cursor.execute(selectStatement)
		connection.commit()
		if cursor.fetchone()[0] < 1:
			return jsonify(r)
		else:
			return "Promotion cannot apply to this account."
	elif r[-1] == 'return user':
		selectStatement = "select count(*) from orders where custid=%s and time < now() - interval '3 months';" % (custid)
		cursor.execute(selectStatement)
		connection.commit()
		if cursor.fetchone()[0] > 0:
			return jsonify(r)
		else:
			return "Promotion cannot apply to this account."
	else:
		return "System error!"

@app.route('/api/v1/apppromotions/addpromo', methods=['POST'])
def add_apppromotion_promo():
	args = request.json

	name = args['name']
	condition = args['condition']
	discType = args['type']
	value = args['value']
	minlimit = args['minlimit']
	maxlimit = args['maxlimit']
	sdate = args['sdate']
	edate = args['edate']
	descript = args['descript']
	sid = args['sid']
	
	try:
		insertStatement = "insert into AppPromotions (discounttype, discount, minlimit, maxlimit, startdatetime, enddatetime, name, description, condition, staffid) select '%s', %s, %s, %s, to_timestamp('%s', 'DD-MM-YY'), to_timestamp('%s', 'DD-MM-YY'), '%s', '%s', '%s', %s where to_date('%s', 'DD-MM-YY') < to_date('%s', 'DD-MM-YY') returning id;" % (discType, value, minlimit, maxlimit, sdate, edate, name, descript, condition, sid, sdate, edate)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	if not cursor.fetchone():
		return 'Invalid input'
	
	return 'pass'

@app.route('/api/v1/apppromotions/updatepromo', methods=['POST'])
def update_apppromotion_promo():
	args = request.json

	pid = args['id']
	name = args['name']
	condition = args['condition']
	discType = args['type']
	value = args['value']
	minlimit = args['minlimit']
	maxlimit = args['maxlimit']
	sdate = args['sdate']
	edate = args['edate']
	descript = args['descript']
	sid = args['sid']
	
	try:
		insertStatement = "update AppPromotions set discounttype='%s', discount=%s, minlimit=%s, maxlimit=%s, startdatetime=to_timestamp('%s', 'DD-MM-YY'), enddatetime=to_timestamp('%s', 'DD-MM-YY'), name='%s', description='%s', condition='%s', staffid=%s where to_timestamp('%s', 'DD-MM-YY') < to_timestamp('%s', 'DD-MM-YY') and id=%s returning id;" % (discType, value, minlimit, maxlimit, sdate, edate, name, descript, condition, sid, sdate, edate, pid)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	if not cursor.fetchone():
		return 'Invalid input'
	
	return 'pass'

@app.route('/api/v1/apppromotions/deletepromo', methods=['POST'])
def delete_apppromotion_promo():
	args = request.json

	pid = args['id']
	
	try:
		statement = "delete from AppPromotions where id=%s;" % (pid)
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	
	return 'pass'

@app.route('/api/v1/restaurantpromotionitems/getlist', methods=['GET'])
def get_restaurantpromotionitems_list():
	promoId = request.args.get('id')
	selectStatement = "select itemid, quantity from restaurantpromotionitems where promoid=%s;" % (promoId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/restaurantpromotions/getlist', methods=['GET'])
def get_restaurantpromotion_list():
	restId = request.args.get('id')
	selectStatement = "select id, code, discounttype, discount, minlimit, maxlimit, name, description, EXTRACT(DAY FROM enddatetime - now()) + 1, TO_CHAR(startdatetime, 'DD-MM-YY'), TO_CHAR(enddatetime, 'DD-MM-YY') from restaurantpromotions where restid=%s and startdatetime <= now() and enddatetime >= now() order by startdatetime asc;" % (restId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/restaurantpromotions/getentry', methods=['GET'])
def get_restaurantpromotion_entry():
	restId = request.args.get('id')
	code = request.args.get('code')
	selectStatement = "select id, code, discounttype, discount, minlimit, maxlimit, name, description from restaurantpromotions where restid=%s AND code='%s' AND startdatetime <= now() and enddatetime >= now();" % (restId, code)
	cursor.execute(selectStatement)
	connection.commit()
	r1 = cursor.fetchone()
	if not r1:
		return "Invalid promotion code."
	selectStatement = "select itemid, quantity from restaurantpromotionitems where promoid=%s;" % (r1[0])
	cursor.execute(selectStatement)
	connection.commit()
	r2 = cursor.fetchall()
	print(r1)
	print(r2)
	print(jsonify((r1, r2)))
	return jsonify((r1, r2))

@app.route('/api/v1/restaurantpromotions/getrestaurantsummary', methods=['GET'])
def get_restaurantpromotions_restaurantsummary():
	restId = request.args.get('id')
	selectStatement = "select name, EXTRACT(DAY FROM enddatetime - startdatetime), (select count(id) from orders where status='completed' and ordertime >= rp1.startdatetime and ordertime <= rp1.enddatetime)/EXTRACT(DAY FROM enddatetime - startdatetime) from restaurantpromotions as rp1 where restid=%s order by name asc;" % (restId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/restaurantpromotions/addpromo', methods=['POST'])
def add_promo():
	args = request.json

	restId = args['id']
	discounttype = args['type']
	discountvalue = args['value']
	promomin = args['min']
	promomax = args['max']
	name = args['name']
	descript = args['description']
	startdate = args['start']
	enddate = args['end']
	items = args['items']

	try:
		float(discountvalue)
		float(promomin)
		float(promomax)
	except Exception as e:
		return 'Invalid input.'

	try:
		insertStatement = "insert into restaurantpromotions (DiscountType, Discount, MinLimit, MaxLimit, StartDateTime, EndDateTime, Name, Description, RestId) values ('%s', %s, %s, %s, '%s', '%s', '%s', '%s', %s) returning Id;" % (discounttype, discountvalue, promomin, promomax, startdate, enddate, name, descript, restId)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	promoId = cursor.fetchone()[0]
	
	partialstatement = ''
	for itemId, qty in items.items():
		if type(qty) is not int:
			try:
				if int(qty) < 1:
					continue
			except Exception as e:
				return 'Invalid input!'
		partialstatement += "(%s, %s, %s)," % (promoId, itemId, qty)
	if partialstatement:
		try:
				statement = "insert into RestaurantPromotionItems (promoid, itemid, quantity) values %s;" % (partialstatement[:-1])
				cursor.execute(statement)
				connection.commit()
		except Exception as e:
			print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
			return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/restaurantpromotions/updatepromo', methods=['POST'])
def update_promo():
	args = request.json

	promoId = args['id']
	discounttype = args['type']
	discountvalue = args['value']
	promomin = args['min']
	promomax = args['max']
	name = args['name']
	descript = args['description']
	startdate = args['start']
	enddate = args['end']
	items = args['items']

	partialstatement = ''
	for itemId, qty in items.items():
		if type(qty) is not int:
			try:
				if int(qty) < 1:
					continue
			except Exception as e:
				return 'Invalid input!'
		partialstatement += "(%s, %s, %s)," % (promoId, itemId, qty)
	if partialstatement:
		partialstatement = partialstatement[:-1]
	
	try:
		statement = "update restaurantpromotions set DiscountType='%s', Discount=%s, MinLimit=%s, MaxLimit=%s, Name='%s', Description='%s', StartDateTime='%s', EndDateTime='%s' where id=%s;" % (discounttype, discountvalue, promomin, promomax, name, descript, startdate, enddate, promoId)
		cursor.execute(statement)
		connection.commit()
		statement = "delete from RestaurantPromotionItems where promoid=%s;" % (promoId)
		cursor.execute(statement)
		connection.commit()
		if partialstatement:
			statement = "insert into RestaurantPromotionItems (promoid, itemid, quantity) values %s;" % (partialstatement)
			cursor.execute(statement)
			connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/restaurantpromotions/deletepromo', methods=['POST'])
def delete_promo():
	args = request.json

	promoId = args['id']

	try:
		insertStatement = "delete from restaurantpromotions where id=%s;" % (promoId)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/orders/getrecentaddr', methods=['GET'])
def get_order_recent_address():
	cid = request.args.get('id')
	selectStatement = "select distinct on (address) address, area from (select address, area from orders where custid=%s order by address, ordertime) as recent order by address asc limit 5;" % (cid)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/orders/getlist', methods=['GET'])
def get_order_list():
	custId = request.args.get('id')
	selectStatement = "select id, reviewid, TO_CHAR(ordertime, 'DD-MM-YY HH12:MI AM'), status, TO_CHAR(coalesce(atcusttime, tocusttime, atresttime, toresttime, ordertime), 'DD-MM-YY HH12:MI AM') from orders where custid=%s and status<>'error' order by ordertime desc;" % (custId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/orders/getrestaurantlist', methods=['GET'])
def get_restaurant_order_list():
	restId = request.args.get('id')
	selectStatement = "select o1.id, TO_CHAR(o1.ordertime, 'DD-MM-YY HH12:MI AM'), oi1.qty, oi1.name from orderitems oi1 left join orders o1 on oi1.orderid=o1.id where o1.restid=%s order by o1.ordertime desc;" % (restId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/orders/getrestaurantname', methods=['GET'])
def get_restaurant_name():
	orderId = request.args.get('id')
	selectStatement = "select name from restaurants where id in (select restid from orders where id=%s);" % (orderId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchone()
	return jsonify(r)

@app.route('/api/v1/orders/getrestaurantsummary', methods=['GET'])
def get_orders_restaurantsummary():
	restId = request.args.get('id')
	selectStatement = "select extract(year from ordertime), extract(month from ordertime), count(id), sum(subtotal-deliveryfee) from orders where restid=%s and status='completed' group by extract(year from ordertime), extract(month from ordertime) order by extract(year from ordertime), extract(month from ordertime);" % (restId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/orders/getrestaurantsummaryfavorite', methods=['GET'])
def get_orders_restaurantsummaryfavorite():
	restId = request.args.get('id')
	year = request.args.get('year')
	month = request.args.get('month')
	selectStatement = "select name from orderitems where orderid in (select id from orders where restid=%s and status='completed' and extract(month from ordertime)=%s and extract(year from ordertime)=%s) group by name order by sum(qty) desc limit 5;" % (restId,month,year)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/orders/getlistrider', methods=['GET'])
def get_orders_rider():
	rid = request.args.get('id')
	result = []
	selectStatement = "select o1.id, r1.name, r1.address, o1.address, o1.status, to_char(coalesce(atcusttime, tocusttime, atresttime, toresttime, ordertime), 'DD-MM-YY HH12:MI AM'), o1.paymethod, o1.total from orders o1 left join restaurants r1 on o1.restid = r1.id where o1.riderid=%s and coalesce(atcusttime, tocusttime, atresttime, toresttime, ordertime) >= all (select coalesce(atcusttime, tocusttime, atresttime, toresttime, ordertime) from orders where riderid=%s);" % (rid, rid)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchone()
	if not r:
		return 'fail'
	result.append(r)
	selectStatement = "select name, qty from orderitems where orderid=%s order by name;" % (r[0])
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	result.append(r)
	return jsonify(result)

@app.route('/api/v1/orders/getfdssummary', methods=['GET'])
def get_orders_fdssummary():
	selectStatement = "(select extract(year from now()) as year, month, (select count(id) from customers where extract(year from registerdate) = extract(year from now()) and extract(month from registerdate) = month), (select count(id) from orders where extract(year from ordertime) = extract(year from now()) and extract(month from ordertime) = month), (select coalesce(sum(total),0) from orders where extract(year from ordertime) = extract(year from now()) and extract(month from ordertime) = month) from generate_series(1,extract(month from now())::INTEGER) as month) UNION (select extract(year from now() - interval '1 year') as year, month, (select count(id) from customers where extract(year from registerdate) = extract(year from now() - interval '1 year') and extract(month from registerdate) = month), (select count(id) from orders where extract(year from ordertime) = extract(year from now() - interval '1 year') and extract(month from ordertime) = month), (select coalesce(sum(total),0) from orders where extract(year from ordertime) = extract(year from now() - interval '1 year') and extract(month from ordertime) = month) from generate_series(1,12) as month) order by year desc, month desc;"
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/orders/statustorest', methods=['POST'])
def update_order_statustorest():
	args = request.json

	rid = args['id']

	try:
		statement = "update orders set riderid=%s, status='torest', toresttime=now() where id = (select id from orders where toresttime is null order by ordertime limit 1) returning id;" % (rid)
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	
	if not cursor.fetchone():
		return "There is no assignemnt at the moment. Try again later."

	return 'pass'

@app.route('/api/v1/orders/statusatrest', methods=['POST'])
def update_order_statusatrest():
	args = request.json

	oid = args['id']

	try:
		statement = "update orders set status='atrest', atresttime=now() where id=%s returning id;" % (oid)
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	
	if not cursor.fetchone():
		return "System error."

	return 'pass'

@app.route('/api/v1/orders/statustocust', methods=['POST'])
def update_order_statustocust():
	args = request.json

	oid = args['id']

	try:
		statement = "update orders set status='tocust', tocusttime=now() where id=%s returning id;" % (oid)
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	
	if not cursor.fetchone():
		return "System error."

	return 'pass'

@app.route('/api/v1/orders/statuscompleted', methods=['POST'])
def update_order_statuscompleted():
	args = request.json

	oid = args['id']

	try:
		statement = "update orders set status='completed', atcusttime=now() where id=%s returning id;" % (oid)
		cursor.execute(statement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	
	if not cursor.fetchone():
		return "System error."

	return 'pass'

@app.route('/api/v1/orders/addorder', methods=['POST'])
def add_order():
	args = request.json

	items = args['cart']
	restId = args['restId']
	custId = args['custId']
	address = args['address']
	area = args['area']
	deliveryFee = args['fee']
	discount = args['discount']
	points = args['point']
	payment = args['payment']

	subTotal = deliveryFee
	for item in items:
		subTotal += item['price'] * item['qty']
	
	total = subTotal - discount - (points * 0.01)

	try:
		insertStatement = "insert into Orders (RestId, CustId, Address, Area, DeliveryFee, PointsUsed, SubTotal, Total,  PayMethod)  values(%s, %s,'%s','%s', %s, %s, %s, %s,'%s') returning Id;" % (restId, custId, address, area, deliveryFee, points, subTotal, total, payment)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	
	orderId = cursor.fetchone()[0]

	for item in items:
		try:
			insertStatement = "insert into orderitems (orderid, unitprice, name, qty) values (%s, %s, '%s', %s);" % (orderId, item['price'], item['name'], item['qty'])
			cursor.execute(insertStatement)
			connection.commit()
		except Exception as e:
			print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
			return 'Unknown error!'
	
	try:
		insertStatement = "update orders set status='ordered' where id=%s;" % orderId
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	return 'pass'

@app.route('/api/v1/reviews/getlist', methods=['GET'])
def get_review_list():
	restId = request.args.get('id')
	selectStatement = "select TO_CHAR(datetime, 'DD-MM-YY HH12:MI AM'), rating, description from reviews where id in (select reviewid from orders where restid=%s) order by datetime desc limit 5;" % (restId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/reviews/addreview', methods=['POST'])
def add_review():
	args = request.json
	orderId = args['id']
	rating = args['rating']
	description = args['description']
	try:
		insertStatement = "insert into reviews (rating, description) values (%s, '%s') returning Id;" % (rating, description)
		cursor.execute(insertStatement)
		connection.commit()
		reviewId = cursor.fetchone()[0]
		insertStatement = "update orders set reviewid=%s where id=%s;" % (reviewId, orderId)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	return 'pass'

@app.route('/api/v1/schedule/getlist', methods=['GET'])
def get_schedule_list():
	rideId = request.args.get('id')
	selectStatement = "select id, to_char(startdate, 'DD-MM-YY'), to_char(enddate, 'DD-MM-YY'), (select count(*) from intervals where scheduleid=s1.id) from schedule as s1 where riderid=%s order by startdate desc;" % (rideId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/schedule/getsalaries', methods=['GET'])
def get_schedule_salaries():
	rideId = request.args.get('id')
	selectStatement = "select to_char(startdate, 'DD-MM-YY'), to_char(enddate, 'DD-MM-YY'), (select count(*) from intervals where scheduleid=s1.id), (select count(*) from orders where riderid=s1.riderid and toresttime >= startdate and toresttime <= enddate), commission + (select salary from riders where id=s1.riderid) from schedule s1 where riderid=%s and enddate < now() order by startdate desc;" % (rideId)
	cursor.execute(selectStatement)
	connection.commit()
	r = cursor.fetchall()
	return jsonify(r)

@app.route('/api/v1/schedule/addparttime', methods=['POST'])
def add_schedule_parttime():
	args = request.json

	rid = args['id']
	sdate = args['sdate']
	timeslots = args['slots']

	if len(timeslots) < 10:
		return 'Not enough work hours. Minimum 10 hours per week.'

	if len(timeslots) > 48:
		return 'Too many work hours. Maximum 48 hours per week.'

	partialStatment = ''
	partialSchedule = {}
	for slot in timeslots:
		if (slot-1) in timeslots and (slot-2) in timeslots:
			return 'Long work hours. Need 1 hour beak for every 2 hours work.'
		shour = slot % 100
		day = (slot - shour)/100
		partialStatment += '(%s, %s, %s, %s),' % (day, shour, shour + 1, 'x')
		if day in partialSchedule:
			partialSchedule[day].append(shour)
		else:
			partialSchedule[day] = [shour]
	partialStatment = partialStatment[:-1]
	for day,hours in partialSchedule.items():
		selectStatement = "select starthour, count(id) from intervals i1 left join schedule s1 on i1.scheduleid=s1.id where to_date('%s' ,'DD-MM-YY') + '%s day'::INTERVAL=startdate + (day || ' day')::INTERVAL group by starthour order by count(id) asc;" % (sdate, day - 1)
		cursor.execute(selectStatement)
		connection.commit()
		rows = cursor.fetchall()
		urgentSlots = list(range(10,22))
		spareSlot = 0
		if rows:
			for row in rows:
				urgentSlots.remove(row[0])
				if row[1] < 5:
					urgentSlots.append(row[0])
		for hour in hours:
			if len(urgentSlots) < 1:
				break
			if hour in urgentSlots:
				urgentSlots.remove(hour)
			else:
				spareSlot += 1
		if len(urgentSlots) > 0 and spareSlot > 0:
			return 'Other timeslot(s) needs people. Recommend timeslot is %s Day %s %s:00 to %s:00.' % (sdate,day,urgentSlots[0],urgentSlots[0]+1)

	try:
		insertStatement = "insert into schedule (riderid, startdate, enddate) select {0}, to_date('{1}', 'DD-MM-YY'), to_date('{1}','DD-MM-YY') + interval '7 days' where not exists (select * from schedule where riderid={1} and (startdate = to_date('{1}', 'DD-MM-YY') or enddate = to_date('{1}', 'DD-MM-YY') or startdate = to_date('{1}','DD-MM-YY') + interval '7 days' or (startdate > to_date('{1}', 'DD-MM-YY') and startdate < to_date('{1}','DD-MM-YY') + interval '7 days') or (enddate > to_date('{1}', 'DD-MM-YY') and enddate < to_date('{1}','DD-MM-YY') + interval '7 days'))) and to_timestamp('{1}', 'DD-MM-YY') > now() returning id;".format(rid, sdate)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	
	rid = cursor.fetchone()

	if not rid:
		return 'Make sure date is entered correctly and does not collide with existing schedules.'

	partialStatment = partialStatment.replace('x', str(rid[0]))

	try:
		insertStatement = "insert into intervals (day, starthour, endhour, scheduleid) values %s;" % (partialStatment)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	return 'pass'

@app.route('/api/v1/schedule/addfulltime', methods=['POST'])
def add_schedule_fulltime():
	args = request.json

	rid = args['id']
	sdate = args['sdate']
	timeslots = args['slots']

	if len(timeslots) < 5:
		return 'Not enough work hours. Minimum 5 days/shifts per week.'
		
	if len(timeslots) > 5:
		return 'Too many work hours. Maximum 5 days/shifts per week.'

	days = [(int(key) - 1) for key in timeslots.keys()]
	days.sort()
	for day in days:
		if (day + 1)%7 not in days and (day + 3)%7 not in days:
			return 'Work days must be in consecutive order.'

	partialStatment = ''
	shiftSlots = [9, 10, 11, 12, 14, 15, 16, 17]
	for day,shift in timeslots.items():
		for x in range(4):
			dday = int(day) + (x * 7)
			selectStatement = "select starthour, count(id) from intervals i1 left join schedule s1 on i1.scheduleid=s1.id where to_date('%s' ,'DD-MM-YY') + '%s day'::INTERVAL=startdate + (day || ' day')::INTERVAL group by starthour order by count(id) asc;" % (sdate, dday - 1)
			cursor.execute(selectStatement)
			connection.commit()
			rows = cursor.fetchall()
			urgentSlots = list(range(10,22))
			spareSlot = 0
			if rows:
				for row in rows:
					urgentSlots.remove(row[0])
					if row[1] < 5:
						urgentSlots.append(row[0])
			for slot in shiftSlots:
				shour = slot + shift
				ehour = shour + 1
				partialStatment += '(%s, %s, %s, %s),' % (dday, shour, ehour, 'x')
				if shour in urgentSlots:
					urgentSlots.remove(shour)
				else:
					spareSlot += 1
			if len(urgentSlots) > 0 and spareSlot > 0:
				return 'Other timeslot(s) needs people. Recommend timeslot is %s Day %s %s:00 to %s:00.' % (sdate,dday,urgentSlots[0],urgentSlots[0]+1)

	partialStatment = partialStatment[:-1]

	try:
		insertStatement = "insert into schedule (riderid, startdate, enddate) select {0}, to_date('{1}', 'DD-MM-YY'), to_date('{1}','DD-MM-YY') + interval '28 days' where not exists (select * from schedule where riderid={1} and (startdate = to_date('{1}', 'DD-MM-YY') or enddate = to_date('{1}', 'DD-MM-YY') or startdate = to_date('{1}','DD-MM-YY') + interval '28 days' or (startdate > to_date('{1}', 'DD-MM-YY') and startdate < to_date('{1}','DD-MM-YY') + interval '28 days') or (enddate > to_date('{1}', 'DD-MM-YY') and enddate < to_date('{1}','DD-MM-YY') + interval '28 days'))) and to_timestamp('{1}', 'DD-MM-YY') > now() returning id;".format(rid, sdate)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'
	
	rid = cursor.fetchone()

	if not rid:
		return 'Make sure date is entered correctly and does not collide with existing schedules.'

	partialStatment = partialStatment.replace('x', str(rid[0]))

	try:
		insertStatement = "insert into intervals (day, starthour, endhour, scheduleid) values %s;" % (partialStatment)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	return 'pass'

@app.route('/api/v1/schedule/delete', methods=['POST'])
def delete_schedule():
	args = request.json
	sid = args['id']

	try:
		insertStatement = "delete from schedule where id=%s and startdate > now() returning id;" % (sid)
		cursor.execute(insertStatement)
		connection.commit()
	except Exception as e:
		print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(e).__name__, e.args))
		return 'Unknown error!'

	if not cursor.fetchone():
		return 'System error. Try again later.'

	return 'pass'

@app.route('/api/v1/intervals/getlistpart', methods=['GET'])
def get_interval_list_part():
	sid = request.args.get('id')
	selectStatement = "select day, starthour from intervals where scheduleid=%s;" % (sid)
	cursor.execute(selectStatement)
	connection.commit()
	rows = cursor.fetchall()
	result = {}
	for row in rows:
		result[row[0]*100 + row[1]] = 'yes'
	return result

@app.route('/api/v1/intervals/getlistfull', methods=['GET'])
def get_interval_list_full():
	sid = request.args.get('id')
	selectStatement = "select day, min(starthour) from intervals where scheduleid=%s group by day limit 5;" % (sid)
	cursor.execute(selectStatement)
	connection.commit()
	rows = cursor.fetchall()
	result = {}
	for row in rows:
		result[str(row[0])] = row[1] - 9
	return result

def flaskThread():
	app.run(host='0.0.0.0', port=8000, debug=False)

def resetItems(): #reset stock every midnight
	while True:
		currentTime = datetime.now().astimezone(timezone('Asia/Singapore')).hour
		isReset = False
		updateStatement = "update FoodItems set CurrentOrders=0"
		
		if not isReset:
			if currentTime > 22 or currentTime < 10:
					cursor.execute(updateStatement)	
					connection.commit()
					
					if cursor.rowcount:
						isReset = True
			
		time.sleep(3600)

if __name__ == '__main__':
	flaskThread = threading.Thread(target=flaskThread, args=())
	flaskThread.start()
	
	resetItemsThread = threading.Thread(target=resetItems, args=())
	resetItemsThread.start()
	