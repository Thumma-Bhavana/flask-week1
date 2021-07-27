from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    # names=["vaishnavi","gupta","palabatla"]
    return render_template("index.html")
    
    # return "Hello world"

# @app.route("/<name>")
# def index(name):

#     return render_template("index.html",name=name)

# @app.route("/<name>")
# def index1(name):
#     return render_template("index.html", name=name)

@app.route("/forms", methods=["POST","GET"])
def forms():
    if(request.method=="GET"):
        return "login again"
    else:
        fname=request.form.get("fname")
        lname=request.form.get("lname")
        return f"{fname} {lname}"

