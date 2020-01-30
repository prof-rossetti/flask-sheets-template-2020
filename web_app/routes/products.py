from web_app.spreadsheet_service import get_products, create_product

from flask import Blueprint, request, render_template, jsonify, flash, redirect #, url_for

product_routes = Blueprint("product_routes", __name__)

@product_routes.route('/products')
def index():
    print("VISITING THE PRODUCTS INDEX PAGE")
    sheet, products = get_products()
    return render_template("products/index.html", products=products, sheet_name=sheet.title)

@product_routes.route('/products/new')
def new():
    print("VISITING THE NEW PRODUCT PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    return render_template("products/form.html")

# move to api:

@product_routes.route('/products/create', methods=["POST"])
def create():
    print("CREATING A PRODUCT...")
    print("FORM DATA:", dict(request.form))
    try:
        product_name = request.form["product_name"]
        product_attributes = {
            "name": product_name,
            "department": request.form["department"],
            "price": request.form["price"],
            "availability_date": request.form["availability_date"]
        }
        response = create_product(product_attributes)
        flash(f"Product '{product_name}' created successfully!", "success") # use the "success" category to correspond with twitter bootstrap alert colors
        return redirect("/products")
    except Exception as err:
        print("ERROR:", type(err), err.name)
        flash(f"ERROR: {err.name}. Please try again.", "danger") # use the "danger" category to correspond with twitter bootstrap alert colors
        return redirect("/products")
