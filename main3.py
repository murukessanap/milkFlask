import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request, redirect
from werkzeug import generate_password_hash, check_password_hash

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




if __name__ == "__main__":
    app.debug = True
    app.run()
