from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:gid>')
class GenreViewById(Resource):
    def get(self, gid):
        return genre_schema.dump(genre_service.get_by_id(gid)), 200