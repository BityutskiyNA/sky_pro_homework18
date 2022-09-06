from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session


    def get_all(self):
        return self.session.query(Movie).all()


    def get_by_id(self, id):
        return self.session.query(Movie).get(id)


    def get_by_director(self, director_id):
        return self.session.query(Movie).filter_by(director_id=director_id).all()


    def get_by_genre(self, genre_id):
        return self.session.query(Movie).filter_by(genre_id=genre_id).all()


    def get_by_year(self, year):
        return self.session.query(Movie).filter_by(year=year).all()


    def new_movie(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie


    def update_movie(self, data):
        m_id = data.get("id")
        movie = self.get_by_id(m_id)
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.session.add(movie)
        self.session.commit()

        return movie


    def delete_movie(self, m_id):
        movie = self.get_by_id(m_id)
        self.session.delete(movie)
        self.session.commit()

        return ""