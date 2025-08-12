from flask import Flask, render_template
import os, json

app = Flask(__name__, static_folder="static", template_folder="templates")

# IMPORTANT for GitHub Pages (makes links work under /YourRepoName/)
app.config["FREEZER_RELATIVE_URLS"] = True

@app.route("/")
def home():
    return render_template("index.html", title="My Restaurant")

@app.route("/menu")
def menu():
    data_path = os.path.join(app.root_path, "data", "menu.json")
    with open(data_path, "r", encoding="utf-8") as f:
        menu_data = json.load(f)
    return render_template("menu.html", title="Menu", menu=menu_data)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True)
