import os 

class Config:
  SECRET_KEY= ' 2345ba6c787654321234a5 c63'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' 
  MAIL_SERVER = 'smtp.google.mail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('EMAIL_USER')
  MAIL_PASSWORD = os.environ.get('EMAIL_PASS')