""" Model schema for SQL table classes """
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()

class HNTopCommentors(db.Model):
    __tablename__ = "HNTopCommentors"
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False)
    order = db.Column(db.Integer,nullable=False)
    author = db.Column(db.String(100), nullable=False)
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    text = db.Column(db.String(2500), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    neg = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    average = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<comment {}>'.format(self.text)