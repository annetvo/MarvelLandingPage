from flask import Blueprint, jsonify
from app.models import Hero, db

api = Blueprint('api', __name__, url_prefix='/api/')

@api.route('/heroes', methods=['GET'])
def heroes():
    heroes = {a.hero:a.to_dict() for a in Hero.query.all()}
    return jsonify(heroes)
