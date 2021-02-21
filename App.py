from flask import Flask,request,render_template,jsonify
from CRUD import fetch, add
import json

#Flask Application
app = Flask(__name__,template_folder='templates')


#Post a feedback from a user to the database with POST Method
@app.route("/feedback", methods=["GET","POST"])
def hello():
    if request.method == 'POST':
        data = add()
        if data == 'added':
            return render_template("center.html")
        else :
            return data

    return render_template("values.html")


#Retrieve all feedbacks in the database with GET Method
@app.route("/added")
def getFeedbacks():
    data = fetch()
    return data

@app.route("/view")
def getData():
    data = fetch()
    print(data)
    return render_template("data.html",value=data)

@app.route("/login", methods=["GET","POST"])
def loggedin():
    if request.method == 'POST':
        if request.form.get("uname") == 'admin' and request.form.get("psw") == 'admin123': 
            data = fetch()
            return render_template("data.html",value=data)
    return render_template("login.html")


@app.route("/")
def func():
    return render_template("website.html")



#Run application server
if __name__ == "__main__":
    app.run()

