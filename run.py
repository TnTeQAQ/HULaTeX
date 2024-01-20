from flask import Flask, redirect, url_for
import config
from backend import backend
from website import website

app = Flask(__name__)

app.register_blueprint(website, url_prefix='/')
app.register_blueprint(backend, url_prefix='/latex2pdf')

if __name__ == '__main__':
    app.run(port=config.PORT, host=config.HOST, debug=config.DEBUG)