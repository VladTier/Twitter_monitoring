#default config
class BaseConfig(object):
    DEBUG = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'my super-puper key'
    SQLALCHEMY_DATABASE_URI = 'mysql://mysqladmin:admin@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = True
