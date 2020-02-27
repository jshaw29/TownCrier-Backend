from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from towncrier import app
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
db = SQLAlchemy(app)
db.create_all()
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    message = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return '<User %r post %r' % self.username,self.message

    def create(u,m):
        ps = Post(username=u,message=m)
        db.session.add(ps)
        db.session.commit()
        return
    def getAll():
        return 