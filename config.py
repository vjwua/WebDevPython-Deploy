import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = b"277764450344399279392461713642952840400"
    #using secrets.SystemRandom().getrandbits(128)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/api_accounts"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///flaskdb.db")

class ProdConfig(Config):
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///flaskdb.db")

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False #!!
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///flask_testdb.db")

config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig,
    'test': TestConfig,
}