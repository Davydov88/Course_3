from flask import request
from flask_restx import Namespace, Resource

from project.services import auth_service, users_service

api = Namespace('auth')


@api_route('/register/')
class AuthView(Resource):
    @api.expect(auth)
    @api.response(201, description='OK')
    def post(self):
        """Регистрация пользователя"""

        user_service.create(request.json)
        return "OK", 201


@api_route('/login/')
class AuthView(Resource):
    @api.expect(auth)
    @api.response(auth_result, code=200)
    def post(self):
        """Аутенфикация пользователя"""

        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            return 'Необходимо ввести логин и пароль', 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 200


    def put(self):
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.generate_tokens(token)

        return tokens, 200


