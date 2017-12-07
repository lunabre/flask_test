from flask_wtf import Form
from wtforms import StringField, TextAreaField, validators


class CommentForm(Form):
    ## declare fields
    author = StringField(
            'Author',
            validators=[
                validators.DataRequired()
                
                ]
            )
    text = TextAreaField(
            'Comment',
            validators=[
                validators.DataRequired()
                ]
            )
