## this contains the views. what is the user going to perceive after execution?
from app import app
from flask import render_template
from .forms import CommentForm


## for this to become a webapp, we need to use routes
## thats what this decorator is doing
@app.route('/hello_world')
def hello_world():
    return 'Hola mundo'

@app.route('/index_template')
def index_template():
    return render_template(
            'index_1.html',
            )

## or i can put it in some other path,
@app.route('/hello_loop') ## works for www.page.com/hola
def hello_loop():
    salsas  = [
            {   'size' : '2 oz',
                'price' : '40',
                'deleted' : False
                },
            {   'size' : '4 oz',
                'price' : '70',
                'deleted' : False
                },
            {   'size' : '5 oz',
                'price' : '85',
                'deleted' : False
                },
            {   'size' : '10 oz',
                'price' : '160',
                'deleted' : False
                },
            {   'size' : '15 oz',
                'price' : '240',
                'deleted' : True
                }
            ]

    
    ## for this name to be considered in the template, i need to send it as parameter
    return render_template(
            'index.html',
            salsas = salsas )


@app.route('/forms_mensajes', methods = ["GET","POST"])
def comment():
    comments = [
            {   'author' : 'chuy',
                'text' : 'What is up'
            
                }
            ]
    form = CommentForm()
    
    if form.validate_on_submit():
        comments.append{
                'author' : form.author.data,
                'text' : form.text.data
                
                }

    return render_template(
            'comments.html',
            comments = comments,
            form = form
            )

