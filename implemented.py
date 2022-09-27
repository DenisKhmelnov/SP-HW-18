# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.movie_service import MovieService
from setup_db import db

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)