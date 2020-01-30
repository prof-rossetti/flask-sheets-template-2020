
from flask import Blueprint, current_app, flash, jsonify, redirect, request, url_for

from web_app.routes.error_handlers import not_found, bad_request
from web_app.spreadsheet_service import SpreadsheetService

ss = SpreadsheetService() # TODO: attach to Flask current_app during app construction in __init__.py

products_api_routes = Blueprint("products_api_routes", __name__)

@products_api_routes.route('/api/products')
@products_api_routes.route('/api/products.json')
def list_products():
    print("LISTING PRODUCTS...")
    sheet, products = get_products()
    response = {
        "sheet_name": sheet.title,
        "products": products
    }
    return jsonify(response)

@products_api_routes.route('/api/products/<int:id>')
@products_api_routes.route('/api/products/<int:id>.json')
def show_product(id):
    print(f"SHOWING PRODUCT {id}")
    sheet, products = ss.get_products()
    try:
        product = [p for p in products if str(p["id"]) == str(id)][0]
        return jsonify(product)
    except IndexError as err:
        response = {"message": f"OOPS. Couldn't find a product with an identifier of {id}. Please try again."}
        return jsonify(response), 404

@products_api_routes.route('/api/products/create', methods=["POST"])
@products_api_routes.route('/api/products/create.json', methods=["POST"])
def create_product():
    # assumes request.method == "POST"
    print("CREATING A PRODUCT...")
    try:
        product_attributes = dict(request.form)
        print("FORM DATA:", product_attributes)
        sheets_response = ss.create_product(product_attributes)
        print(sheets_response)
        #response = {"message": f"Product '{product_attributes['name']}' created successfully!"}
        #return jsonify(response), 200
        flash(f"Product '{product_attributes['name']}' created successfully!", "success")
        return redirect("/products")
    except Exception as err:
        print(err)
        response = {"message": "Server Error. Please try again."}
        return jsonify(response), 500



#@products_api_routes.route('/api/products/<int:id>', methods=["PUT", "POST"])
#@products_api_routes.route('/api/products/<int:id>.json', methods=["PUT", "POST"])
#def update_product(id):
#    current_app.logger.info(f"UPDATING PRODUCT {id}")
#
#    products = read_products_from_file(current_app.config["CSV_FILENAME"])
#    product = find_product(id, products)
#    if product == None:
#        return not_found(message="OOPS. Couldn't find a product with that identifier ({id}). Please try again.")
#
#    edited_product = request.get_json(force=True) # doesn't require request headers to specify content-type of json
#    current_app.logger.info(edited_product)
#    edited_product["id"] = id # don't allow client to overwrite id :-)
#    if is_valid_price(edited_product["price"]) == False:
#        return bad_request(message=f"OOPS. That product price is not valid ({edited_product['price']}). Expecting a price like 4.99 or 0.77. Please try again.")
#
#    products[products.index(product)] = edited_product
#    write_products_to_file(products=products, filename=current_app.config["CSV_FILENAME"])
#    return jsonify(edited_product)
#
#@products_api_routes.route('/api/products/<int:id>', methods=["DELETE"])
#@products_api_routes.route('/api/products/<int:id>.json', methods=["DELETE"])
#def destroy_product(id):
#    current_app.logger.info(f"DESTROYING PRODUCT {id}")
#
#    products = read_products_from_file(current_app.config["CSV_FILENAME"])
#    product = find_product(id, products)
#    if product == None:
#        return not_found(message="OOPS. Couldn't find a product with that identifier ({id}). Please try again.")
#
#    del products[products.index(product)]
#    write_products_to_file(products=products, filename=current_app.config["CSV_FILENAME"])
#    return jsonify({"message": "Product Deleted Successfully"})
#
