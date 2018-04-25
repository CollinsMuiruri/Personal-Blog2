import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # simple mde configuration
    SIMPLEMDE_JS_FILE = True
    SIMPLEMDE_USE_CDN = True
    UPLOADED_PHOTOS_DEST  ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collins:wildgoosechase@localhost/blogs'
    SECRET_KEY="0717745223"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={
"production":ProdConfig,
"development":DevConfig
}
