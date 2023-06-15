from flask import Flask,render_template,redirect,request,session
import mysql.connector

app = Flask(__name__)  

@app.route("/")
def loginpage():
      return  render_template("loginpage.html")

@app.route("/mainpage")
def mainpage():
      return render_template("mainpage.html")
    
@app.route("/Showrecords",methods=["GET","POST"])
def Showrecords():
        mydb=mysql.connector.connect(
              host="localhost",
              user="root",
              password="1234",
              database="login")
        cursor=mydb.cursor()
        sql="select * from coordinates"
        cursor.execute(sql,)
        records=cursor.fetchall()
        return render_template("Showrecords.html",dept=records)

if(__name__ == "__main__"):
  app.run(debug=True)
  