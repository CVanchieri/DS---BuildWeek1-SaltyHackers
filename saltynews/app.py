# imports.
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from saltynews import bigquery

# function for app.
def create_app():
    app = Flask(__name__)
    # set the DQL to postgress connection.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ibnzqkfl:rYgeprTJq6jD_eR0bxEXwAnYX7fM-yRD@rajje.db.elephantsql.com:5432/ibnzqkfl'
    DB = SQLAlchemy(app)
    

# landing page route.
    @app.route('/')
    def root():
        # create the dataframe with 30,000 rows, ElephantSQL limits it 20MB.
        HNcommentsDB = client.list_rows(comments_table, max_results=30000).to_dataframe()
        
        

        return (HNcommentsDB.head())


# user search route.
    @app.route('/user', methods=['POST'])
    #@app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        #name = name or request.values['by']

        return ("This will be a 'user' page , lists their comments and saltiness.")






# return/complete the 'app'.
    return app