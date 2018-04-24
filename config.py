import os


class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # simple mde configuration
    SIMPLEMDE_JS_FILE = True
    SIMPLEMDE_USE_CDN = True



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collins:wildgoosechase@localhost/blog'

config_options ={"production":ProdConfig,"development":DevConfig}
