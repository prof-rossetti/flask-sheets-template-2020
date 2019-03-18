
from flask import Blueprint, request, render_template, jsonify

product_routes = Blueprint("product_routes", __name__)

@product_routes.route('/products')
def index():
    print("VISITING THE PRODUCTS INDEX PAGE")
    return render_template("products/index.html")

@product_routes.route('/products/new')
def new():
    print("VISITING THE NEW PRODUCT PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    return render_template("products/form.html")

@product_routes.route('/products/create', methods=["POST"])
def create():
    print("CREATING A PRODUCT...")
    print("FORM DATA:", dict(request.form))
    return jsonify(request.form)
