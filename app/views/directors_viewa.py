from flask_restx import Resource, Namespace

from app.dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@directors_ns.route('/')
class DirectorView(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_all()), 200


@directors_ns.route('/<int:did>')
class DirectorViewById(Resource):
    def get(self, did):
        return director_schema.dump(director_service.get_by_id(did)), 200