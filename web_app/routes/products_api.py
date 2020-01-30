
from flask import Blueprint, current_app, flash, jsonify, redirect, request, url_for

from web_app.routes.error_handlers import not_found, bad_request
from web_app.spreadsheet_service import get_products, create_product

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
    sheet, products = get_products()
    try:
        product = [p for p in products if str(p["id"]) == str(id)][0]
        return jsonify(product)
    except IndexError as err:
        print("ERR", err)
        message = f"OOPS. Couldn't find a product with an identifier of {id}. Please try again."
        response = {"status": 404, "message": message}
        return jsonify(response)





#@products_api_routes.route('/api/products', methods=["POST"])
#@products_api_routes.route('/api/products.json', methods=["POST"])
#def create_product():
#    #current_app.logger.info("CREATING PRODUCT")
#    #new_product = request.get_json(force=True) # doesn't require request headers to specify content-type of json
#    #if is_valid_price(new_product["price"]) == False:
#    #    return bad_request(message=f"OOPS. That product price is not valid ({new_product['price']}). Expecting a price like 4.99 or 0.77. Please try again.")
#    #products = read_products_from_file(current_app.config["CSV_FILENAME"])
#    #new_product["id"] = auto_incremented_id(products)
#    #products.append(new_product)
#    #write_products_to_file(products=products, filename=current_app.config["CSV_FILENAME"])
#    #return jsonify(new_product)
#
#    #print("CREATING A PRODUCT...")
#    #print("FORM DATA:", dict(request.form))
#    #try:
#    #    product_name = request.form["product_name"]
#    #    product_attributes = {
#    #        "name": product_name,
#    #        "department": request.form["department"],
#    #        "price": request.form["price"],
#    #        "availability_date": request.form["availability_date"]
#    #    }
#    #    response = create_product(product_attributes)
#    #    flash(f"Product '{product_name}' created successfully!", "success") # use the "success" category to correspond with twitter bootstrap alert colors
#    #    return redirect("/products")
#    #except Exception as err:
#    #    print("ERROR:", type(err), err.name)
#    #    flash(f"ERROR: {err.name}. Please try again.", "danger") # use the "danger" category to correspond with twitter bootstrap alert colors
#    #    return redirect("/products")
#
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
