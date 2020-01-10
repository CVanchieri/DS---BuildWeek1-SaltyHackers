# imports.
from flask import Flask, request, render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

# function for app.
def create_app():
    app = Flask(__name__)
    # set the DQL to postgress connection.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ibnzqkfl:rYgeprTJq6jD_eR0bxEXwAnYX7fM-yRD@rajje.db.elephantsql.com:5432/ibnzqkfl'
    db = SQLAlchemy(app)
    

# landing page route.
    @app.route('/')
    def root():
        # create the dataframe with 30,000 rows, ElephantSQL limits it 20MB.
        
        
        
        return render_template('base.html', title='Home')


# user search route.
    @app.route('/username', methods=['GET'])
    #@app.route('/user/<name>', methods=['GET'])
    def get_user(username):
        db_user = db.select([HNTopComments.columns.author, HNTopComments.columns.rating, HNTopComments.columns.ranking]).where(HNTopComments.columns.author == 'username')
        
        return {"username":author, "negativity score":rating, "negativity rank":ranking}

# return/complete the 'app'.
    return app