from flask import Flask
from flask_assets import Environment, Bundle
from controller import routes

app = Flask(__name__, template_folder='view/templates', static_folder='view/static')
assets = Environment(app)

css = Bundle('css/styles/*.css', filters='cssmin', output='css/styles.min.css')
assets.register('cssmin', css)

# Adicionar filters='jsmin' para minificar
js = Bundle('js/scripts/*.js', output='js/scripts.min.js')
assets.register('jsmin', js)

routes.init(app)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)