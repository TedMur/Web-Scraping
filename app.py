# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
conn = "mongodb://localhost:27017/mars_app"
client = pymongo.MongoClient(conn)

@app.route("/")
def index():
    mars = client.db.mars.find_one()
    return render_template('index.html', mars=mars)

@app.route("/scrape")
def scrape():
    mars = client.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return  redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    