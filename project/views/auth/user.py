from flask import request
from flask_restx import Resource, Namespace

from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser
from project.services import auth_service, users_service


user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        all_users = user_service.get_all()

        return all_users, 200


    def post(self):
        data = request.json
        user = user_service.create(data)
        return "", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @auth_required
    def get(self, uid):
        user = user_service.get_one(uid)

        return user, 200

    @admin_required
    def put(self, uid):
        data = request.json
        if 'id' not in data:
            data['id'] = uid
        user_service.update(data)
        return "", 204

    @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204



