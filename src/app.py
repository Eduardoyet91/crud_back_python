from flask import Flask
#from flask_cors import CORS
from flask_cors import CORS

from config import config

# Routes
from router import User

app = Flask(__name__)

cors= CORS(app, resources={r"*": {"origins": "http://localhost:3000"}})


#def page_not_found(error):
 #   return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(User.main, url_prefix='/')

    # Error handlers
    #app.register_error_handler(404, page_not_found)
    app.run()
