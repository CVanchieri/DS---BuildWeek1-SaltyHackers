""" Model schema for SQL table classes """

from saltynews import bigquery

db = bigquery

class User(db.Model):
    user_name = db.Column(db.String(100), primary_key=True)
    date_created = db.Column(db.Integer)
    salty_rank = db.Column(db.Float, nullable=False)
    salty_comments = db.Column(db.Integer, nullable=False)
    comments_total = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User {self.user_name} -- Salty Ranking {self.salty_rank}"

    def serialize_user(self):
        """ serialize object to return JSON format """
        return {
            "user_name" : self.user_name,
            "date_created" : self.date_created,
            "salty_rank" : self.salty_rank,
            "salty_comments" : self.salty_comments,
            "comments_total" : self.comments_total
        }


class Comments(db.Model):
    comment_uuid = db.Column(db.BigInteger, primary_key=True)
    user_name = db.Column(db.String(100), db.ForeignKey('user.user_name'))
    is_salty = db.Column(db.Integer)
    text = db.Column(db.String(2500))
    date_created = db.Column(db.BigInteger)

    def __repr__(self):
        return f"User {self.user_name} -- Said: {self.text}"

    def serialize_comments(self):
        """ serialize object to return JSON format """
        return {
            "comment_uuid" : self.comment_uuid,
            "uesr_name" : self.user_name,
            "is_salty" : self.is_salty,
            "text" : self.text,
            "date_created" : self.date_created
        }
