from flask import Flask
from flask_restx import Api
from config import ConfigApi
from app.setup_db import db
from app.views.directors_viewa import directors_ns
from app.views.genre_viewa import genre_ns
from app.views.movie_viewa import movie_ns
from create_data import data_create

app_config = ConfigApi()


def create_app(config: ConfigApi):
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    data_create()

app = create_app(app_config)



if __name__ == '__main__':
    app.run()
