from flask import Blueprint,render_template

edmin_blueprint = Blueprint('edmin_blueprint', __name__)

# class Countries(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name= db.Column(db.String(50)) 

@edmin_blueprint.route('/index')
def index():
    return render_template("index.html")








# @edmin_blueprint.route('/adduser')
# def adduser():
     # return render_template("addUser.html")

@edmin_blueprint.route('/listUser')
def listuser():
     return render_template("listUser.html")