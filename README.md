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

## Usage

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
