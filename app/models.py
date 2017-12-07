## where models are like tables

from app import db 

class Comment(db.Model):
    id = db.Column(
            db.Integer,
            primary = True
            )

    autor = db.Column(
            db.String(30), 
            index = False, 
            unique = False
            )

    text = db.Column(
            db.Text, 
            index = False, 
            unique = False
            )
