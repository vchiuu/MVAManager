from mvaManager.config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database, drop_database

def resetdb():
  if database_exists(Config.DB_URL):
    print('Deleting database.')
    drop_database(Config.DB_URL)
  if not database_exists(Config.DB_URL):
    print('Creating database.')
    create_database(Config.DB_URL)