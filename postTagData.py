from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQALCHEMY_DATABASE_USI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


tag = db.Table('tag',
               db.Column('infoOne', db.Integer, db.ForeignKey(' 
