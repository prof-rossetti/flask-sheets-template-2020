# adapted from: https://github.com/prof-rossetti/products-api-flask/blob/csv/products_api/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home import home_routes
from web_app.routes.products import product_routes
from web_app.routes.products_api import products_api_routes

load_dotenv()

FLASK_ENV = os.environ.get("FLASK_ENV", "development") # set to "production" in the production environment
SECRET_KEY = os.environ.get("SECRET_KEY", "my super secret") # overwrite this in the production environment
TESTING = False # True if app_env == "test" else False

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(ENV=FLASK_ENV, SECRET_KEY=SECRET_KEY, TESTING=TESTING)
    app.register_blueprint(home_routes)
    app.register_blueprint(product_routes)
    app.register_blueprint(products_api_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True) # debug mode allows you to see printed content in development environment
