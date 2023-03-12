from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import status_page_parser

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    @movie_ns.expect(status_page_parser)
    @movie_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """Получение всех фильмов"""

        return movie_service.get_all(**page_parser.parse_args())


@movie_ns.route('/<int:director_id>')
class MovieView(Resource):
    @movie_ns.response(404, 'Not Found')
    @movie_ns.marshal_with(movie, code=200, description='ok')
    def get(self, director_id: int):
        """Получение фильма по id"""
        return movie_service.get_one(director_id)
