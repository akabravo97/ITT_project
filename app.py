from flask import Flask, render_template,redirect,url_for, request,session
import sqlite3


app = Flask(__name__)
app.secret_key = 'yolo'





@app.route("/")
def init():
    return render_template('index.html')

@app.route("/register",methods = ['POST', 'GET'])
def register():
	message=''
	#database init
	conn=sqlite3.connect("ITT.db")
	if request.method == 'POST':
		username = str(request.form['name']);
		password = str(request.form['password']);
		email    = str(request.form['email']);
		emailpass = str(request.form['emailpass']);
		
				
		#Insert
		if conn.execute("INSERT into details values(?,?,?,?)",(username,password,email,emailpass)):
			message="You have been successfully Registered!"
		else:
			message="Error! Please try again"

	conn.commit()
	conn.close();
	return render_template('index.html',result=message);

@app.route("/login",methods = ['POST', 'GET'])
def login():
	#database init
	conn=sqlite3.connect("ITT.db")
	message=''
	if request.method == 'POST':
		username = str(request.form['nameL']);
		password = str(request.form['passwordL']);

		content=conn.cursor()
		content.execute("SELECT * from details where username=? and password=? ",(username,password));
		cursor=content.fetchall()


		if len(cursor)==1:
			#return render_template for dashboard.html and replace return render_template
			for row in cursor:

				session['email']=row[2];
				session['emailpass']=row[3];

			conn.close();
			return "done!"

		else:
			conn.close();
			message='User not registered!'
			return render_template('index.html',result=message)
	

if __name__ == "__main__":
    app.run()
