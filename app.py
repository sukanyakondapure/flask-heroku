from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message

# from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config.from_pyfile('config.py')
mail = Mail(app)
db = SQLAlchemy(app)
# ma = Marshmallow(app)


from views import *
from api import *

if __name__=='__main__':
    app.run(debug=True)