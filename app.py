# app.py

from flask import Flask
from config import Config
from extensions import db
from routes.main import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    with app.app_context():
        # Register Blueprints
        app.register_blueprint(main_blueprint)

        # Create database tables if they don't exist
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)