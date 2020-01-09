
from flask import Flask, jsonify, render_template
from flask_json import FlaskJSON, json_response
from saltynews import app
from saltynews.models import User, Comments


@app.route('/user', methods=['POST'])
def user():
    """ API call for user table """
    user_query = user.query.all()
    user = [user.serialize_user() for user in user_query]
    return jsonify(user)


@app.route('/comments', methods=['POST'])
def comments():
    """ API call for comments table """
    comments_query = Comments.query.all()
    comments = [comment.serialize_comments() for comment in comments_query]
    return jsonify(comments)
