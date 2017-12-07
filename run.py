## this file makes sure the app is always accessible
from app import app


## we use debug as True only during development stage
## this will prokove the error details to be promted in
## both the terminal and the client
app.run(debug=True)
