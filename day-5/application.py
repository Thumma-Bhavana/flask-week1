from flask import Flask,render_template, request
# from flask.wrappers import Request

app=Flask(__name__)

@app.route("/")
def demo():
    return render_template("index.html")

@app.route("/forms", methods=["POST"])
def forms():

    if(request.method=="GET"):
        return f"Hello you are ready to use the application"
    else:
        fname=request.form.get("fname")
        lname=request.form.get("lname")
        

        return f"Hello {fname} {lname}, you are ready to use the application"