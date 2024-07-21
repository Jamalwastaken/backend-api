#!/usr/bin/env python3

import connexion
from flask import jsonify

from swagger_server import encoder
from swagger_server.db import db



connex_app = connexion.App(__name__, specification_dir='./swagger/')
connex_app.app.json_encoder = encoder.JSONEncoder
connex_app.add_api('swagger.yaml', arguments={'title': 'Swagger Petstore - OpenAPI 3.0'}, pythonic_params=True)

app = connex_app.app

username = "postgres"
password = "1234"
dbname = "main_db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.before_first_request
def create_tables():
    db.create_all()

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    }), 400

@app.errorhandler(404)
def bad_request(error):
    return jsonify({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    }), 404

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    db.init_app(app)
    app.run(port=8080)
