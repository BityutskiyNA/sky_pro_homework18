from app.dao.directorDAO import DirectorDAO


class DirectorService:
    def __init__(self, dao:DirectorDAO):
        self.dao = dao


    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, id):
        return self.dao.get_by_id(id)

