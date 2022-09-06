# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)
from app.dao.directorDAO import DirectorDAO
from app.dao.genreDAO import GenreDAO
from app.dao.movieDAO import MovieDAO
from app.service.directorSRV import DirectorService
from app.service.genreSRV import GenreService
from app.service.movieSRV import MovieService
from app.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

