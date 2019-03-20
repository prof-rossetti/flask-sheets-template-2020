# Starter Web App (Flask)

An example web application, built in Python with the Flask package, with a Google Sheets datastore, for educational purposes.

Deployment Environments:

version | branch | production_url
--- | --- | ---
Basic | master | https://web-app-starter-flask.herokuapp.com/
Google Sheets Datastore | sheets | https://web-app-starter-flask-sheets.herokuapp.com/products

## Installation

Clone or download from [GitHub source](https://github.com/prof-rossetti/web-app-starter-flask). And navigate there from the command-line:

```sh
cd starter-web-app-flask
```

Create and activate an Anaconda virtual environment:

```sh
conda create -n web-starter-env # first time only
conda activate web-starter-env
```

> NOTE: Subsequent commands assume you're running them from within the virtual environment, in the root directory of the repository.

Install package dependencies (first time only):

```sh
pip install -r requirements.txt
```

## Setup

### Google Sheets

> SEE ALSO: this [excellent blog post](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)

#### Downloading Credentials

Visit the [Google Developer Console](https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the [API Credentials](https://console.developers.google.com/apis/credentials) page, follow a process to generate and download credentials to use the APIs. Fill in the form to find out what kind of credentials:

  + API: "Google Sheets API"
  + Calling From: "Web Server"
  + Accessing: "Application Data"
  + Using Engines: "No"

The suggested credentials will be for a service account. Follow the prompt to create a new service account with a role of: "Project" > "Editor", and create credentials for that service account. Finally, download the resulting .json file and store it in this repo as "auth/spreadsheet_credentials.json".

#### Configuring a Spreadsheet Datastore

Use this [example Google Sheet datastore](https://docs.google.com/spreadsheets/d/1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE/edit#gid=0) (document id: `1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE`), or create your own Google Sheet.

If you create your own, make sure it contains a sheet called "Products" with column headers `id`, `name`, `department`, `price`, and `availability_date`. And modify the document's sharing settings to grant "edit" privileges to the "client email" address located in the credentials file.

Note the document's unique identifier from its URL, and store the identifier in an environment variable called `GOOGLE_SHEET_ID`.

## Usage

Send some test data to and from google sheets:

```sh
python app/spreadsheet_service.py
```

Run a local web server, then view your app in a browser at http://localhost:5000/:

```sh
FLASK_APP=web_app flask run
```

> NOTE: you can quit the server by pressing ctrl+c at any time. If you change a file, you'll likely need to restart the server for the changes to take effect.


## Deploying

First, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and make sure you can login and list your applications.

```sh
heroku login

heroku apps:list
```

### Deploying the Basic App

Create a new application server, optionally specifying a name (e.g. "web-app-starter-flask"):

```sh
heroku apps:create web-app-starter-flask # or do this from the online console
```

Then associate this repository with that application, as necessary:

```sh
heroku git:remote -a web-app-starter-flask # necessary if you created the app from the online console
```

After this configuration process is complete, you should be able to "deploy" the application's source code to the Heroku server:

```sh
git push heroku master
```

## [Licence](/LICENSE.md)
