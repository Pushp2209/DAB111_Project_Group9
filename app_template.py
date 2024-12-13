from flask import Flask, render_template
import sqlite3
from pathlib import Path
import os

# Configure paths
base_path = Path().cwd()
db_name = "Orders.db"
db_path = base_path / db_name

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/data")
def data():
    # Connect to the database and fetch data
    con = sqlite3.connect("Orders.db")
    cursor = con.cursor()
    
    # Fetch data
    orders = cursor.execute("SELECT * FROM Orders limit 10 ").fetchall()
    con.close()

    return render_template("data.html", orders=orders)


if __name__ == "__main__":
    app.run(debug=True)
