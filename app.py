from flask import Flask, render_template
from api import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api/v1')

@app.route("/")
def hello_world():
    return render_template('index.html')