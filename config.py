# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

# Пример

class ConfigApi:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

