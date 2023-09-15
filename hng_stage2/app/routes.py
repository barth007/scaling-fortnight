from app.models import User
from flask import jsonify, Blueprint, request, make_response, abort
from app import db, csrf



bp = Blueprint('user', __name__)


@bp.route('/api/<param>', methods=['GET'])
def get_user(param):
    if param.isdigit():
        user_id = int(param)
        user = User.query.get(user_id)
    else:
        user = User.query.filter_by(name=param).first()
    if user is None:
        abort(not_found(404, "User Not Found"))
    response = {
            "id": user.id,
            "name": user.name,
            "email":user.email
        }
    return jsonify(response)


@bp.route('/api', methods=['POST'])
@csrf.exempt
def create_user():
    data = request.get_json()
    if 'name' not in data or 'email' not in data:
        abort(bad_request(400, "Name and Email must be included"))
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"User Created Sucessfully!"}), 201


@bp.route('/api/<param>', methods=['PUT'])
@csrf.exempt
def update(param):
    if param.isdigit():
        user_id = int(param)
        user = User.query.get(user_id)
    else:
        user = User.query.filter_by(name=param).first()
    if user is None:
        abort(not_found(404, "User Not Found"))
    data = request.get_json()
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    return  jsonify({"message":"Updated Successfully!"}), 200


@bp.route('/api/<param>', methods=['DELETE'])
@csrf.exempt
def delete(param):
    if param.isdigit():
        user_id = int(param)
        user = User.query.get(user_id)
    else:
        user = User.query.get(param)
    if user is None:
        abort(not_found(404, "User Not Found"))
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message":"User Deleted!"}), 200


@bp.errorhandler(400)
def bad_request(error, message):
    return make_response(jsonify({'error': message}), 400)


@bp.errorhandler(404)
def not_found(error, message):
    return make_response(jsonify({'error': message}), 404)
