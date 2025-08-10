from app import app
from flask_frozen import Freezer

app.config['FREEZER_DESTINATION'] = 'docs'   # put the static site into docs/
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
