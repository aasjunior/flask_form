from flask import Flask
from controller import routes

app = Flask(__name__, template_folder="view/templates")

routes.init(app)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)