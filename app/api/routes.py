from flask import Blueprint, json, jsonify, request
from flask.wrappers import Response
from app.models import Hero, db

api = Blueprint('api', __name__, url_prefix='/api/')

@api.route('/heroes', methods=['GET'])
def heroes():
    heroes = {a.hero:a.to_dict() for a in Hero.query.all()}
    return jsonify(heroes)


@api.route('/heroes/<int:id>')
def get_hero(id):
    try:
        hero = Hero.query.get(id).to_dict()
        return jsonify(hero)
    except:
        return jsonify(f'Hero of id: <{id}> does not exist in the database')


@api.route('/heroes/<int:id>', methods=['DELETE'])
def delete_hero(id):
    try:
        hero = Hero.query.get(id)
        db.session.delete(hero)
        db.session.commit()
        return jsonify({'Deleted': hero.to_dict()})
    except:
        return jsonify(f'Hero of id: <{id}> does not exist in the database')


@api.route('/heroes/<int:id>', methods=['PUT'])
def update_hero(id):
    response = request.get_json()
    print(response)
    hero = Hero.query.get(id)
    hero.from_dict(response)
    print(hero.to_dict())
    db.session.commit()
    return jsonify({'Updated': hero.to_dict()})



@api.route('createhero',methods=['POST'])
def create_hero():
    r = request.get_json()
    newHero = Hero()
    newHero.from_dict(r)
    print(newHero.to_dict())
    db.session.add(newHero)
    db.session.commit()
    return jsonify({'Created': newHero.query.all()[-1].to_dict()})