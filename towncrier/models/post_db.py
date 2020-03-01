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
        posts = Post.query.all()
        return jsonify([Post.serialize(post) for post in posts])
    def getUser(name):
        posts = Post.query.filter_by(username=str(name))
        return jsonify([Post.serialize(post) for post in posts])
    def deleteAll():
        Post.query.delete()
        db.session.commit()
        return jsonify({"success":True})
    def serialize(self):
        return {
            'username': self.username,
            'message': self.message,
        }