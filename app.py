from flask import Flask,render_template,request,redirect,url_for
import sqlite3
app=Flask(__name__)
@app.route('/')
def second():
        return render_template('reg1.html')
@app.route('/success/<username>/<email>')
def Success(username,email):
	conn=sqlite3.connect('fine.db')
	conn.execute("drop table if exists student")
	conn.execute("create table student(username TEXT ,email email)")
	conn.execute('''INSERT OR REPLACE INTO student(username,email) VALUES(?,?)''', (username,email))
	conn.commit()
	return render_template('reg1.html',message='SUCCESSFULLY UPDATED')
@app.route('/fetchdata',methods=['POST','GET'])
def FetchData():
        if request.method=="POST":
                user1=request.form['username']
                e=request.form['email']
                return redirect(url_for('Success',username=user1,email=e))
        else:
                user1=request.args.get('username')
                e=request.form.get('email')
                return redirect(url_for('Success',username=user1,email=e))

if __name__=="main_":
        app.run(debug=True)
