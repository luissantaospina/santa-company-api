from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://' +\
        config('PGSQL_USER') + ':' +\
        config('PGSQL_PASSWORD') + '@' + \
        config('PGSQL_HOST') + ':' + \
        config('PGSQL_PORT') + '/' + \
        config('PGSQL_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
