from flask import Flask, request, jsonify, _request_ctx_stack
from flask_migrate import Migrate
from flask_cors import cross_origin, CORS
from .config import Config
from .model import db, Form

app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db.init_app(app)
Migrate(app, db)


@app.route("/")
@cross_origin(headers=["Content-Type"])
def public():
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return jsonify(message=response)


@app.route("/form", methods=['POST'])
def formInfo():
    data = request.json
    info = Form(
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        phone = data['phone'],
        company = data['company'],
        state = data['state'],
        role = data['role']
    )
    db.session.add(info)
    db.session.commit()
    return 'added successfully', 201
