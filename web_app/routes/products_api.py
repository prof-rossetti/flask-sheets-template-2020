
from flask import Blueprint, current_app, flash, jsonify, redirect, request, url_for

#from web_app.routes.error_handlers import not_found, bad_request
from web_app.spreadsheet_service import SpreadsheetService

products_api_routes = Blueprint("products_api_routes", __name__)

@products_api_routes.route('/api/products', methods=["GET"])
@products_api_routes.route('/api/products.json', methods=["GET"])
def list_products():
    print("LISTING PRODUCTS...")
    sheet, products = ss.get_products()
    response = {"sheet_name": sheet.title, "products": products}
    return jsonify(response)

@products_api_routes.route('/api/products', methods=["POST"])
@products_api_routes.route('/api/products.json', methods=["POST"])
def create_product():
    print("CREATING A PRODUCT...")
    product_attrs = dict(request.form)
    print("FORM DATA:", product_attrs)

    ss = current_app.config['SPREADSHEET_SERVICE']
    sheets_response = ss.create_product(product_attrs)
    print(sheets_response)

    if request.path.endswith(".json"):
        return jsonify({"message": f"Product '{product_attrs['name']}' created successfully!"}), 200
    else:
        flash(f"Product '{product_attrs['name']}' created successfully!", "success")
        return redirect(f"/products") # or maybe to: f"/products/{product_attrs['id']}"

@products_api_routes.route('/api/products/<int:id>', methods=["GET"])
@products_api_routes.route('/api/products/<int:id>.json', methods=["GET"])
def show_product(id):
    print(f"SHOWING PRODUCT {id}")
    ss = current_app.config['SPREADSHEET_SERVICE']
    try:
        product = ss.get_product(id)
        print(product)
        return jsonify(product)
    except IndexError as err:
        return jsonify({"message": f"OOPS. Couldn't find a product with an identifier of {id}. Please try again."}), 404

@products_api_routes.route('/api/products/<int:id>', methods=["PUT", "POST"])
@products_api_routes.route('/api/products/<int:id>.json', methods=["PUT", "POST"])
def update_product(id):
    print(f"UPDATING PRODUCT {id}")
    product_attrs = request.get_json(force=True) # doesn't require request headers to specify content-type of json
    product_attrs["id"] = id # don't allow client to overwrite id :-)
    print(product_attrs)

    ss = current_app.config['SPREADSHEET_SERVICE']
    sheets_response = ss.update_product(product_attrs)
    print(sheets_response)

    if request.path.endswith(".json"):
        return jsonify({"message": f"Product '{product_attrs['name']}' updated successfully!"}), 200
    else:
        flash(f"Product '{product_attrs['name']}' updated successfully!", "success")
        return redirect(f"/products/{id}")

@products_api_routes.route('/api/products/<int:id>', methods=["DELETE"])
@products_api_routes.route('/api/products/<int:id>.json', methods=["DELETE"])
def destroy_product(id):
    print(f"DESTROYING PRODUCT {id}")

    ss = current_app.config['SPREADSHEET_SERVICE']
    sheets_response = ss.destroy_product(id)
    print(sheets_response)

    if request.path.endswith(".json"):
        return jsonify({"message": "Product destroyed!"}), 200
    else:
        flash(f"Product destroyed!", "success")
        return redirect("/products")
