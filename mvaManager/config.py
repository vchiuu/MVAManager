import os 

class Config:
  SECRET_KEY= ' 2345ba6c787654321234a5 c63'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  POSTGRES_URL = 'postgres://buwyfojbbjvnvj:46196cce065cc13493fdb4c0d5a4f53c72cacac9a5e2d5b4edfeacdc609ec673@ec2-107-22-160-185.compute-1.amazonaws.com:5432/da63o1tatim54q'
  POSTGRES_USER = 'buwyfojbbjvnvj'
  POSTGRES_PW = '46196cce065cc13493fdb4c0d5a4f53c72cacac9a5e2d5b4edfeacdc609ec673'
  POSTGRES_DB = 'da63o1tatim54q'
  DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
  MAIL_SERVER = 'smtp.google.mail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('EMAIL_USER')
  MAIL_PASSWORD = os.environ.get('EMAIL_PASS')