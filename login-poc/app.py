from flask import *
import os


app = Flask(__name__)

username = "shayan"
password = "shayan"

@app.route("/", methods=["GET", "POST"])
def f1():
    p = ""
    
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    
    if username == "None" or password == "None":
        p = ""
        
    elif username == "shayan" and password == "shayan":
        p = "Login successful"
        
    else:
        p = "Username or Password is wrong"
        
    return render_template("index.html", p=p, username=username, password=password)



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)