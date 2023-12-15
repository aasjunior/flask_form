from flask_assets import Environment, Bundle
from os import getenv
from dotenv import load_dotenv

load_dotenv()
secret_key = getenv('SECRET_KEY')

def config_app(app):
    app.config['DEBUG'] = True

    # Set secret key for CSRF protection.
    app.config['SECRET_KEY'] = secret_key

    compress_minify_files(app)


def compress_minify_files(app):
    '''
        Compress and minify CSS and JS files
    '''
    assets = Environment(app)

    css = Bundle('css/styles/*.css', filters='cssmin', output='css/styles.min.css')
    assets.register('cssmin', css)

    # Adicionar filters='jsmin' para minificar
    js = Bundle('js/scripts/*.js', output='js/scripts.min.js')
    assets.register('jsmin', js)
