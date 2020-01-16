# Data-Science

# API:
We are using the API through BigQuery, this allows us to access 30,000 rows of comments, it seems to be random on order unfortunately but at least its something to work with.


# Rest API Usage
---------------

## User Rank and Overall negativity route
--------------------------------------
end of url: /user/*username*

Takes a username, and returns the username, an average negativity score of that user, and the user's negativity rank.
Will return error if not given a string. 

Example response(Passed): {"username": "Iloch, "neg_score": 0.12, "neg_rank": 10}
Example response(Failed): {'Status': 'Failed'}

## Comment scoring route
--------------------------
end of url: /comments/*comment*

Takes a comment and returns the negativity score for it. 

Example response(Passed): {"neg_score": .24}
Example response(Failed): {'Status': 'Failed'}





