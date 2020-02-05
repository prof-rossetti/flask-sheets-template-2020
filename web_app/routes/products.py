
from flask import Blueprint, request, render_template, jsonify, flash, redirect, current_app #, url_for

product_routes = Blueprint("product_routes", __name__)

@product_routes.route('/products')
def index():
    print("VISITING THE PRODUCTS INDEX PAGE")
    ss = current_app.config['SPREADSHEET_SERVICE']
    sheet, products = ss.get_products()
    return render_template("products/index.html", products=products, sheet_name=sheet.title, sheet_id= ss.sheet_id)

@product_routes.route('/products/new')
def new():
    print("VISITING THE NEW PRODUCT PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    return render_template("products/form.html")

@product_routes.route('/products/<int:id>')
def show(id):
    print("VISITING THE PRODUCT SHOW PAGE", id)
    ss = current_app.config['SPREADSHEET_SERVICE']
    product = ss.get_product(id)
    return render_template("products/show.html", product=product)

@product_routes.route('/products/<int:id>/edit')
def edit(id):
    print("VISITING THE EDIT PRODUCT FORM", id)
    ss = current_app.config['SPREADSHEET_SERVICE']
    product = ss.get_product(id)
    return render_template("products/edit_form.html", product=product)
