from flask_frozen import Freezer
from app import app

# Make sure relative URLs are used in the frozen site
app.config["FREEZER_RELATIVE_URLS"] = True

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
