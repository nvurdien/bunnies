import os
from credentials import *

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    port = str(5432)
    SQLALCHEMY_DATABASE_URI = 'postgresql://'+user+':'+passwd+'@'+hostname+':'+port+'/'+db_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = False 
    DEBUG = False 


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = False 


class TestingConfig(Config):
    TESTING = False 
