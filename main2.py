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


@app.route('/add', methods=['POST'])
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



@app.route('/update', methods=['PUT'])
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


@app.route('/delete/<username>')
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



if __name__ == "__main__":
    app.debug = True
    app.run()
