import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request, redirect
from werkzeug import generate_password_hash, check_password_hash

@app.route('/names')
def names():
	#cursor=None
	#conn=None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM name;")
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


if __name__ == "__main__":
    app.debug = True
    app.run()
