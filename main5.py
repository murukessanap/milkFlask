import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request, redirect
from werkzeug import generate_password_hash, check_password_hash
import datetime as dt

@app.route('/users')
def users():
	#cursor=None
	#conn=None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM credentials;")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		pass

@app.route('/')
def default():
	try:
		return "Welcome";
	except Exception as e:
		print(e)


@app.route('/adduser', methods=['POST'])
def add_user():
	try:		
		_username = request.form['username']
		_password = request.form['password']
		_designation = request.form['designation']
		#_designation = int(_designation)
		print(type(_designation))
		# validate the received values
		if _username and _password and request.method == 'POST':
			#do not save password as a plain text
			#_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO credentials(username, password, designation) VALUES(%s, %s, %s)"
			data = (_username, _password, _designation)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('User added successfully!')
			return redirect('/')
		else:
			return 'Error while adding user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



@app.route('/updateuser', methods=['PUT'])
def update_user():
	try:		
		_username = request.form['username']
		_password = request.form['password']
		_id = request.form['id']
		# validate the received values
		if _username and _password and _id and request.method == 'PUT':
			#do not save password as a plain text
			#_hashed_password = generate_password_hash(_password)
			#print(_hashed_password)
			# save edits
			sql = "UPDATE credentials SET username=%s, password=%s WHERE username=%s"
			data = (_username, _password, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('User updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/deleteuser/<username>')
def delete_user(username):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM credentials WHERE username=%s", (username,))
		conn.commit()
		flash('User deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/milksuppliers')
def milkSuppliers():
	#cursor=None
	#conn=None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM milk_supplier;")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		pass



@app.route('/addsupplier', methods=['POST'])
def add_supplier():
	try:		
		_supname = request.form['supplier_name']
		# validate the received values
		if _supname and request.method == 'POST':
			sql = "INSERT INTO milk_supplier(sup_name) VALUES(%s)"
			data = (_supname)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('supplier added successfully!')
			return redirect('/')
		else:
			return 'Error while adding user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/updatesupplier', methods=['PUT'])
def update_supplier():
	try:		
		_supcode = request.form['sup_code']
		_supname = request.form['sup_name']
		# validate the received values
		if _supcode and _supname and request.method == 'PUT':
			#do not save password as a plain text
			#_hashed_password = generate_password_hash(_password)
			#print(_hashed_password)
			# save edits
			sql = "UPDATE milk_supplier SET sup_name=%s WHERE sup_code=%s"
			data = (_supname, _supcode,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('supplier updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



@app.route('/deletesupplier/<sup_code>')
def delete_supplier(sup_code):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM milk_supplier WHERE sup_code=%s", (sup_code,))
		conn.commit()
		flash('supplier deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/rates')
def rates():
	#cursor=None
	#conn=None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM rate;")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		pass


@app.route('/addrate', methods=['POST'])
def add_rate():
	try:		
		_fat = request.form['fat']
		_snf = request.form['snf']
		ts_rate = '220.0'
		_rate = (float(_fat)+float(_snf))*(float(ts_rate)/100.0)
		print("rate=",_rate)
		# validate the received values
		if _fat and _snf and _rate and request.method == 'POST':
			sql = "INSERT INTO rate(fat,snf,rate) VALUES(%s,%s,%s)"
			data = (_fat,_snf,_rate)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('rate added successfully!')
			return redirect('/')
		else:
			return 'Error while adding rate'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



@app.route('/updaterate', methods=['PUT'])
def update_rate():
	try:		
		_fat = request.form['fat']
		_snf = request.form['snf']
		_rate = request.form['rate']
		# validate the received values
		if _fat and _snf and _rate and request.method == 'PUT':
			#do not save password as a plain text
			#_hashed_password = generate_password_hash(_password)
			#print(_hashed_password)
			# save edits
			sql = "UPDATE rate SET rate=%s WHERE fat=%s AND snf=%s"
			data = (float(_rate), float(_fat), float(_snf))
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('rate updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating rate'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



@app.route('/deleterate/<fat>/<snf>')
def delete_rate(fat,snf):
	try:
		print("fat,snf",fat,snf)
		sql = "DELETE FROM rate WHERE fat=%s AND snf=%s"
		data = (float(fat),float(snf))
		print(data)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		flash('rate deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



@app.route('/milkpurchases')
def purchases():
	#cursor=None
	#conn=None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM milk_purchase;")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		pass



@app.route('/addpurchase', methods=['POST'])
def add_purchase():
	try:	
		_date = request.form['date']
		format_str = '%d/%m/%Y' # The format
		_datetime = dt.datetime.strptime(_date, format_str)

		_shift = request.form['shift']
		_sup_code = int(request.form['supplier_code'])
		_sup_name = request.form['supplier_name']
		_quantity = float(request.form['qty'])
		_fat = float(request.form['fat'])
		_snf = float(request.form['snf'])
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT rate FROM rate WHERE fat=%s AND snf=%s;",(_fat,_snf))
		rate = cursor.fetchall()
		print(rate)
		_rate = float(rate[0]['rate'])
		print(_rate)
		_amount = _rate * _quantity
		print(_amount)
		#_rate = 0.0
		print("rate=",_rate)
		# validate the received values
		if _datetime and _shift and _sup_code and _sup_name and _quantity and _fat and _snf and _rate and _amount and request.method == 'POST':
			sql = "INSERT INTO milk_purchase(date,shift,sup_code,sup_name,qty,fat,snf,rate,amount) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			data = (_datetime, int(_shift), _sup_code, _sup_name, _quantity, _fat, _snf, _rate, _amount)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('purchase added successfully!')
			return redirect('/')
		else:
			return 'Error while adding rate'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/updatepurchase', methods=['PUT'])
def update_purchase():
	try:		
		_date = request.form['date']
		format_str = '%d/%m/%Y' # The format
		_datetime = dt.datetime.strptime(_date, format_str)
		print(_datetime)
		_shift = request.form['shift']
		_sup_code = request.form['supplier_code']
		_sup_name = request.form['supplier_name']
		_qty = request.form['qty']
		_fat = request.form['fat']
		_snf = request.form['snf']
		_rate = request.form['rate']
		_amount = request.form['amount']
		print(_amount)		
		# validate the received values
		if _datetime and _shift and _sup_code and _sup_name and _qty and _fat and _snf and _rate and _amount and request.method == 'PUT':
			#do not save password as a plain text
			#_hashed_password = generate_password_hash(_password)
			#print(_hashed_password)
			# save edits
			print(_amount)
			sql = "UPDATE milk_purchase SET sup_name=%s,qty=%s,fat=%s,snf=%s,rate=%s,amount=%s WHERE date=%s AND shift=%s AND sup_code=%s"
			data = (_sup_name, float(_qty), float(_fat), float(_snf), float(_rate), float(_amount), _datetime, int(_shift), int(_sup_code))
			print(data)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('purchase updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating rate'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



@app.route('/deletepurchase/<date>/<shift>/<sup_code>')
def delete_purchase(date,shift,sup_code):
	try:
		print("date,shit,sup_code",date,shift,sup_code)
		sql = "DELETE FROM milk_purchase WHERE date=%s AND shift=%s AND sup_code=%s"
		format_str = '%d-%m-%Y' # The format
		_datetime = dt.datetime.strptime(date, format_str)
		print(_datetime)
		data = (_datetime, int(shift), int(sup_code))
		#print(data)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		flash('purchase deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


if __name__ == "__main__":
    app.debug = True
    app.run()
