from flask import Flask, render_template
import os, json

app = Flask(__name__, static_folder="static", template_folder="templates")

# So links work when the site is hosted at /YourRepoName/ on GitHub Pages
app.config["FREEZER_RELATIVE_URLS"] = True

def load_menu():
    data_path = os.path.join(app.root_path, "data", "menu.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html", title="My Restaurant")

@app.route("/menu.html")
def menu():
    return render_template("menu.html", title="Menu", menu=load_menu())

@app.route("/contact.html")
def contact():
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True)
