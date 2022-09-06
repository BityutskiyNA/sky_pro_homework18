from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service
from app.dao.model.movie import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return movies_schema.dump(movie_service.get_all(request.args)), 200


    def post(self):
        req_json = request.json
        movie = movie_service.get_by_id(req_json.get("id"))
        if not movie:
            movie_n = movie_service.new_movie(req_json)
            return movie_schema.dump(movie_n), 204

        return "Элемент с таким id есть в базе", 404



@movie_ns.route('/<int:mid>')
class MoviesViewById(Resource):
    def get(self, mid):
        return movie_schema.dump(movie_service.get_by_id(mid)), 200

    def put(self, mid):
        movie = movie_service.get_by_id(mid)
        if not movie:
            return "Нет таково кино", 404
        req_json = request.json
        movie_service.update_movie(req_json)
        return "успех", 204

    def delete(self, mid):
        movie = movie_service.get_by_id(mid)
        if not movie:
            return "Нет таково кино", 404
        movie_service.delete_movie(mid)
        return "успех", 204

