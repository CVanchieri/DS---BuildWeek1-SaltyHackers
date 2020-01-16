# imports.
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import pickle as pkl
from .models import db, HNTopCommentors

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



#FLASK_APP=saltyhackers:APP FLASK_ENV=development flask run

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ibnzqkfl:rYgeprTJq6jD_eR0bxEXwAnYX7fM-yRD@rajje.db.elephantsql.com:5432/ibnzqkfl' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy()
some_engine = create_engine('postgres://ibnzqkfl:rYgeprTJq6jD_eR0bxEXwAnYX7fM-yRD@rajje.db.elephantsql.com:5432/ibnzqkfl')
# create a configured "Session" class
Session = sessionmaker(bind=some_engine)
# create a Session
session = Session()
db.init_app(app)

def create_app():
    """Create and configure an instance of the Flask application"""

    @app.route('/')
    def root():

        return ('SaltyHackers!')


    # user search route.
    @app.route('/user/<string:username>', methods=['GET', 'PUSH'])
    def get_user(username):
        if type(username) is str:
            #queries the database for that authors comments
            author_comments = session.query(HNTopCommentors.author, HNTopCommentors.text, HNTopCommentors.neg, HNTopCommentors.ranking, HNTopCommentors.average).first()
            #print(author_comments)
            # Grabs authors rank
            ranking = author_comments.ranking#.ranking needs to be finished.
            # Grabs authors average neg score
            avg_negative = author_comments.average#.average needs to be finished.
            # Returns data in json format
            return jsonify({"UserName": username, "Negative Score": avg_negative, "negative Rank": ranking})
            #return jsonify({"Last Comment": author_comments})
        return jsonify({"Status": 'Failed'})


    # comment negativity scoring route
    @app.route('/comments/<string:comment>', methods=['GET', 'PUSH'])
    def comments(comment):
        if type(comment) is str:
            # Open and read pickled model
            with open('model.pkl', 'rb') as file:
                # Load it into a useable format
                model = pkl.load(file)
            # Use the model on given comment
            neg, neu, pos, rating = model.polarity_scores(comment)
            # Return score in json
            return jsonify({'comment': comment, 'neg_score': neg}) 
        return jsonify({'Status': 'Failed'})

    return app


