
# adapted from: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

from dotenv import load_dotenv
import os

import gspread
from gspread.exceptions import SpreadsheetNotFound
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

DOCUMENT_KEY = os.environ.get("GOOGLE_SHEET_ID", "OOPS Please get the spreadsheet identifier from its URL")
SHEET_NAME = "Products"

#
# AUTHORIZATION
# ... https://developers.google.com/sheets/api/guides/authorizing
# ... https://gspread.readthedocs.io/en/latest/oauth2.html
#

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "spreadsheet_credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

def get_products():
    return [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

if __name__ == "__main__":
    pass

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

    #
    # READ SHEET VALUES
    #

    client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

    doc = client.open_by_key(DOCUMENT_KEY) #> <class 'gspread.models.Spreadsheet'>

    print("-----------------")
    print("SPREADSHEET:", doc.title)
    print("-----------------")

    sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>

    rows = sheet.get_all_records() #> <class 'list'>

    for row in rows:
        print(row) #> <class 'dict'>

    #
    # WRITE VALUES TO SHEET
    #

    next_id = len(rows) + 1 # number of records, plus one. TODO: max of current ids, plus one
    next_row_number = len(rows) + 2 # number of records, plus a header row, plus one

    product = {
        "id": next_id,
        "name": f"Product {next_id}",
        "department": "snacks",
        "price": 4.99,
        "availability_date": "2019-01-01"
    }

    next_row = list(product.values())

    response = sheet.insert_row(next_row, next_row_number)

    print("ADDING A RECORD...")
    # print(type(response)) #> dict
    # print(response) #> {'spreadsheetId': 'abc123', 'updatedRange': 'Products!A5:C5', 'updatedRows': 1, 'updatedColumns': 3, 'updatedCells': 3}

    print(f"UPDATED RANGE: '{response['updatedRange']}' ({response['updatedCells']} CELLS)")
