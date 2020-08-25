import os


email = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')
secretkey = os.environ.get('SECRET_KEY')
sqlalchemydatabaseuri = os.environ.get('SQLALCHEMY_DATABASE_URI')


class Config:
	SECRET_KEY= secretkey
	SQLALCHEMY_DATABASE_URI = sqlalchemydatabaseuri
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_DEBUG = True
	MAIL_USERNAME = email
	MAIL_PASSWORD = password
