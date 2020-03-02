from towncrier import app
from towncrier.models.post_db import Post
from flask import request,jsonify
import os
@app.route('/')
def index():
    return jsonify({"status": "Server is running"})
@app.route('/api/v1/posts',methods=['GET','POST','DELETE'])
def posts():
    if request.method == 'GET':
        return Post.getAll(),200
    elif request.method == 'POST':
        body = request.json
        if "username" not in body.keys() or "message" not in body.keys():
            return jsonify({"Message":"Please format posts correctly","error code":1111}),400
        username = body["username"]
        message = body["message"]
        Post.create(username,message)
        return jsonify({"success":True})
    elif request.method == 'DELETE':
        body = request.json
        secret_key = os.getenv("SECRET_DELETE_KEY")
        if  body == None or "key" not in body.keys():
            return jsonify({"Message":"Please send delete key","error code":1112}),400
        if secret_key != body["key"]:
            return jsonify({"Message":"Invalid Key","error code":1113}), 400
        return Post.deleteAll(),200

@app.route('/api/v1/posts/<username>',methods=['GET'])
def posts_by_user(username):
    return Post.getUser(username)