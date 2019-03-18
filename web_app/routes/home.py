
from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITING THE INDEX PAGE")
    #return "You have visited the homepage"
    return render_template("index.html")

# GET /hello
# GET /hello?name=Polly
@home_routes.route("/hello")
def hello(name=None):
    print("VISITING THE HELLO PAGE")
    print("REQUEST PARAMS:", dict(request.args))

    if "name" in request.args:
        name = request.args["name"]
        message = f"Hello, {name}"
    else:
        message = "Hello World"

    #return message
    return render_template("hello.html", message=message)
