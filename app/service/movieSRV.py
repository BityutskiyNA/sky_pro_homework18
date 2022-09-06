from app.dao.movieDAO import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao


    def get_all(self, request_args):
        if len(request_args) == 0:
            return self.dao.get_all()
        else:
            if genre_id := request_args.get('genre_id'):
                return self.get_by_genre(genre_id)
            elif director_id := request_args.get('director_id'):
                return self.get_by_director(director_id)
            elif year := request_args.get('year'):
                return self.get_by_year(year)



    def get_by_id(self, id):
        return self.dao.get_by_id(id)


    def get_by_director(self, director_id):
        return self.dao.get_by_director(director_id)


    def get_by_genre(self, genre_id):
        return self.dao.get_by_genre(genre_id)


    def get_by_year(self, year):
        return self.dao.get_by_year(year)


    def new_movie(self, data):
        return self.dao.new_movie(data)


    def update_movie(self, data):
        return self.dao.update_movie(data)


    def delete_movie(self, m_id):
        return self.dao.delete_movie(m_id)

