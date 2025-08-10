from flask import Flask, render_template, url_for, request, redirect
import json

app = Flask(__name__)

# Load menu from JSON
def load_menu():
    with open("data/menu.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    menu_data = load_menu()
    return render_template("menu.html", menu=menu_data)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    # If you want to process contact submissions server-side, you'd handle POST here.
    # We'll just show the page. For GitHub Pages (static) we recommend Formspree.
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
