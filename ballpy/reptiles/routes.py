from flask import Blueprint, request, jsonify
from ballpy.models import Reptile, db

bp = Blueprint('reptiles', __name__)

@bp.route('/', methods=['GET'])
def get_reptiles():
    reptiles = Reptile.query.all()
    return jsonify([reptile.to_dict() for reptile in reptiles])

@bp.route('/<int:id>', methods=['GET'])
def get_reptile(id):
    reptile = Reptile.query.get_or_404(id)
    return jsonify(reptile.to_dict())

@bp.route('/', methods=['POST'])
def add_reptile():
    data = request.get_json() or {}
    required_fields = ("common_name", "scientific_name", "conservation_status", "native_habitat")

    if not all(key in data for key in required_fields):
        missing_keys = [key for key in required_fields if key not in data]
        return jsonify({"error": f"Missing data: {', '.join(missing_keys)}"}), 400

    new_reptile = Reptile(
        common_name=data['common_name'],
        scientific_name=data['scientific_name'],
        conservation_status=data['conservation_status'],
        native_habitat=data['native_habitat'],
        fun_fact=data.get('fun_fact', 'No fun fact available')
    )
    db.session.add(new_reptile)
    db.session.commit()
    return jsonify(new_reptile.to_dict()), 201
