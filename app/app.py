from flask import Flask
from controller import routes
from config import config_app

app = Flask(__name__, template_folder='view/templates', static_folder='view/static')

config_app(app)
routes.init(app)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)