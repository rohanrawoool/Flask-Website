from flask import Flask,render_template,request
import mysql.connector


app = Flask(__name__)


conn=mysql.connector.connect(host="localhost",user="root",password="",database="app")
cursor= conn.cursor()



#Home 
@app.route('/')
def login():
    
    return render_template('login.html')



#Registration route
@app.route('/register')
def about():
    return render_template('register.html')


#home page route
@app.route('/print')
def hello():
    return render_template("home.html")



#if Logged_in
@app.route('/login_validation',methods=['get','post'])
def login_validation():
    email= request.form.get('email')
    password = request.form.get('password')
    cursor.execute("""select * from info where email like '{}' and password like '{}'""".format(email,password))
    us= cursor.fetchall()
    if len(us)>0:
        return render_template('testing1.html')
    else:
        return render_template('login.html',info="Invalid User")
        


#Add New user
@app.route('/add_user',methods=['post','get'])
def add_user():
    name= request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    cursor.execute("""insert into info (name,email,password) values('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    return render_template("login.html")



#Contactus
@app.route('/contact',methods=['post','get'])
def contact():
    name= request.form.get('iname')
    number=request.form.get('inumber')
    email=request.form.get('iemail')
    message=request.form.get('imessage')
    cursor.execute("""insert into  contact(name,number,email,message) values('{}','{}','{}','{}')""".format(name,number,email,message))
    conn.commit()
    return "<h1 style='color:pink'>Thanks for connecting with us.....!</h1>"

@app.route('/show_products',methods=['get','post'])
def show():
    return render_template("hello.html")



   

#Run App
if __name__=="__main__":
   app.run()
