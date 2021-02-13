from flask import Flask,render_template,request
from pymongo import MongoClient

client =MongoClient("YOUR MONGODB DATABASE")
db = client["auth"]
collection = db["users"]

app = Flask(__name__) 
 

@app.route('/')

def home():
    return  render_template('landing.html')

@app.route('/register')
def signup():
    return render_template('register.html')

@app.route('/dashboard')
def login():

    #check state 
    return render_template('dashboard.html')
   

@app.route("/login_validation" , methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    state = 0 

    checker = collection.find({"email":email})
    for result in checker :
        if password == result["password"]:
            print("auth done==============")
            state = 1
            return render_template('dashboard.html')
        else : 
            print('auth denied============')
            state = 0   
        return "password wrong"


@app.route("/registration_validate" ,methods=['POST'])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    post ={
        "name" :name ,
        "email": email,
        "password" : password
    }

    collection.insert_one(post)


    return render_template('landing.html')


if __name__ == "__main__":
    app.run(debug=True)








