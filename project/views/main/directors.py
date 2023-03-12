from flask_restx import Namespace, Resource

from project.container import director_service
from project.setup.api.models import director
from project.setup.api.parsers import page_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):
    @director_ns.expect(page_parser)
    @director_ns.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """Получение всех режиссеров"""

        return director_service.get_all(**page_parser.parse_args())


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    @director_ns.response(404, 'Not Found')
    @director_ns.marshal_with(director, code=200, description='ok')
    def get(self, director_id: int):
        """Получение режиссера по id"""
        return director_service.get_one(director_id)
