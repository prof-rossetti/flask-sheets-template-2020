from web_app.spreadsheet_service import get_products

from flask import Blueprint, request, render_template, jsonify, flash, redirect #, url_for

product_routes = Blueprint("product_routes", __name__)

@product_routes.route('/products')
def index():
    print("VISITING THE PRODUCTS INDEX PAGE")
    products = get_products()
    return render_template("products/index.html", products=products)

@product_routes.route('/products/new')
def new():
    print("VISITING THE NEW PRODUCT PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    return render_template("products/form.html")

@product_routes.route('/products/create', methods=["POST"])
def create():
    print("CREATING A PRODUCT...")
    print("FORM DATA:", dict(request.form))
    product_name = request.form["product_name"]
    flash(f"Product '{product_name}' created successfully!", "success") # use the "success" category to correspond with twitter bootstrap alert colors
    return redirect("/products")
