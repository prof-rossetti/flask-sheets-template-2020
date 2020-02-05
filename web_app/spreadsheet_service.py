
# adapted from:
# ... https://developers.google.com/sheets/api/guides/authorizing
# ... https://gspread.readthedocs.io/en/latest/oauth2.html
# ... https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# ... https://github.com/s2t2/birthday-wishes-py/blob/master/app/sheets.py

import json
import os
import random

from dotenv import load_dotenv
import gspread
from gspread.exceptions import SpreadsheetNotFound
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

DOCUMENT_KEY = os.environ.get("GOOGLE_SHEET_ID", "OOPS Please get the spreadsheet identifier from its URL")
SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", default="Products")

#CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "spreadsheet_credentials.json")
GOOGLE_API_CREDENTIALS = os.environ.get("GOOGLE_API_CREDENTIALS")
AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

class SpreadsheetService():
    def __init__(self):
        print("INITIALIZING NEW SPREADSHEET SERVICE...")
        #self.credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
        self.credentials = ServiceAccountCredentials._from_parsed_json_keyfile(json.loads(GOOGLE_API_CREDENTIALS), AUTH_SCOPE)
        self.client = gspread.authorize(self.credentials) #> <class 'gspread.client.Client'>
        self.sheet_id = DOCUMENT_KEY
        self.sheet_name = SHEET_NAME
        self.sheet = None
        self.products = None

    def get_products(self):
        print("GETTING PRODUCTS FROM THE SPREADSHEET...")
        doc = self.client.open_by_key(self.sheet_id) #> <class 'gspread.models.Spreadsheet'>
        self.sheet = doc.worksheet(self.sheet_name) #> <class 'gspread.models.Worksheet'>
        self.products = self.sheet.get_all_records() #> <class 'list'>
        return self.sheet, self.products

    def create_product(self, product_attributes):
        print("NEW PRODUCT ATTRIBUTES:", product_attributes)

        self.get_products()
        print(f"DETECTED {len(self.products)} EXISTING PRODUCTS")
        next_row_number = len(self.products) + 2 # number of records, plus a header row, plus one

        if len(self.products) == 0:
            next_id = 1
        else:
            next_id = max([int(p["id"]) for p in self.products]) + 1

        product = {
            "id": next_id,
            "name": product_attributes["name"],
            "department": product_attributes["department"],
            "price": float(product_attributes["price"]),
            "availability_date": product_attributes["availability_date"],
            "img_url": product_attributes["img_url"]
        }
        next_row = list(product.values()) #> [13, 'Product CLI', 'snacks', 4.99, '2019-01-01']
        response = self.sheet.insert_row(next_row, next_row_number)
        return response

    def get_product(self, product_id):
        """
        Will raise IndexError if product identifier not found in the list
        Otherwise will return the product as a dictionary
        """
        if not (self.sheet and self.products): self.get_products()
        matching_products = [p for p in self.products if str(p["id"]) == str(product_id)]
        return matching_products[0]

    def update_product(self, product_id, product_attributes):
        #product = self.get_product(product_attributes['id'])
        #breakpoint()
        print("TODO UPDATE ROW")
        return True

    def destroy_product(self, product_id):
        #breakpoint()
        print("TODO DELETE ROW")
        return True

if __name__ == "__main__":

    ss = SpreadsheetService()

    sheet, products = ss.get_products()
    print("----------------------")
    print(f"LISTING PRODUCTS FROM THE '{sheet.title}' SHEET")
    for product in products:
        print(product)

    print("----------------------")
    print("CREATING A PRODUCT...")

    IMG_URLS = [
        "https://i.pinimg.com/originals/ea/56/e3/ea56e3ce387edc4fb87963b0c6d757a1.png",
        "https://cdn1.iconfinder.com/data/icons/grocery-supermarket-line/64/grocery_supermarket_shopping_vegetable_food_-512.png",
        "https://cdn1.iconfinder.com/data/icons/shopping-essentials/32/grocery-food-groceries-shop-shopping-milk-512.png",
        "https://cdn2.iconfinder.com/data/icons/shop-until-you-drop/60/groceries-512.png",
        "https://cdn.onlinewebfonts.com/svg/img_566093.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNiqJ8VByiXqMr_kd0C1fY0umMsdasvHAqm6dDWrbfql6pxsQHww&s"
    ]

    product_attributes = {
        "name": "Product CLI",
        "department": "snacks",
        "price": 4.99,
        "availability_date": "2019-01-01",
        "img_url": random.choice(IMG_URLS)
    }

    response = ss.create_product(product_attributes)
    # print(response) #> {'spreadsheetId': 'abc123', 'updatedRange': 'Products!A5:C5', 'updatedRows': 1, 'updatedColumns': 3, 'updatedCells': 3}
    print(f"... UPDATED RANGE: '{response['updatedRange']}' ({response['updatedCells']} CELLS)")

    product_id = products[-1]["id"]
    print("----------------------")
    print("GETTING PRODUCT:", product_id)

    print("----------------------")
    print("EDITING PRODUCT:", product_id)

    print("----------------------")
    print("DELETING PRODUCT:", product_id)
