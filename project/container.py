from project.dao import GenresDAO, MoviesDAO, DirectorsDAO
from project.dao import UserDAO

from project.services import GenresService, MoviesService, DirectorsService

from project.services.users_service import UsersService

from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)
director_dao = DirectorsDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
user_service = UsersService(user_dao)

