from towncrier import app
from towncrier.models.post_db import Post
from flask import request,jsonify
import os
@app.route('/api/v1/posts',methods=['GET','POST'])
def posts():
    if request.method == 'GET':
        return os.getenv("TEST")
    elif request.method == 'POST':
        body = request.json
        if "username" not in body.keys() or "message" not in body.keys():
            return jsonify({"Message":"Please format posts correctly","error code":1111}),400
        username = body["username"]
        message = body["message"]
        Post.create(username,message)
        return str(username)+" sent a message\n",200