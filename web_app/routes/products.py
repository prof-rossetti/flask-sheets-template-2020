
from flask import Blueprint, request, render_template, jsonify, flash, redirect #, url_for
product_routes = Blueprint("product_routes", __name__)

from web_app.spreadsheet_service import SpreadsheetService
ss = SpreadsheetService() # TODO: attach to Flask current_app during app construction in __init__.py

@product_routes.route('/products')
def index():
    print("VISITING THE PRODUCTS INDEX PAGE")
    sheet, products = ss.get_products()
    return render_template("products/index.html", products=products, sheet_name=sheet.title, sheet_id="1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE")

@product_routes.route('/products/new')
def new():
    print("VISITING THE NEW PRODUCT PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    return render_template("products/form.html")

@product_routes.route('/products/<int:id>')
def show(id):
    print("VISITING THE PRODUCT SHOW PAGE", id)
    product = ss.get_product(id)
    return render_template("products/show.html", product=product)

@product_routes.route('/products/<int:id>')
def edit(id):
    print("VISITING THE EDIT PRODUCT FORM", id)
    product = ss.get_product(id)
    return render_template("products/form.html", product=product)
