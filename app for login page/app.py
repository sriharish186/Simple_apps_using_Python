from flask import Flask, render_template, request
import pickle

#from werkzeug.datastructures import RequestCacheControl
app = Flask(__name__)

@app.route('/') 
def hello_world():
    return render_template('login.html')
database={'harish':'1234','joel':'1234'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info="Invalid User")
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info="Invalid Password")
        else:
            return render_template('home.html',name=name1)    

if __name__=="__main__":
    app.run(debug=True)
