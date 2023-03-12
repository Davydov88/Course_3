from typing import Optional

from project.dao.movie import MoviesDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        """Сервис получения одного фильма"""

        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Movie]:
        """Сервис получения всех фильмов"""

        return self.dao.get_all_by_filter(page=page, status=status)
