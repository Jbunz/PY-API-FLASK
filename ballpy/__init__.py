from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('ballpy.config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)

    from ballpy.reptiles.routes import bp as reptiles_bp
    app.register_blueprint(reptiles_bp, url_prefix='/reptiles')

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Reptiles API!"})

    return app
