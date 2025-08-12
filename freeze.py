from app import app
from flask_frozen import Freezer

# Build into /docs for GitHub Pages
app.config["FREEZER_DESTINATION"] = "docs"
# Use relative links so /YourRepoName/ works
app.config["FREEZER_RELATIVE_URLS"] = True

freezer = Freezer(app)

if __name__ == "__main__":
    print("FREEZE FILE:", __file__)
    print("URL MAP:", app.url_map)
    freezer.freeze()
