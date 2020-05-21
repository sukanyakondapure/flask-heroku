from app import app,db,mail
from flask import request,jsonify, make_response, redirect,render_template,flash,url_for
from models import User_new,Countries,States,Cities,User
import uuid
import jwt
import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
from forms import RegistrationForm,LoginForm,UserForm
from flask_mail import Mail, Message

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=None

        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']
            print(token)
        if not token:
            return '<h1>Token Missing</h1>', 401
        
        try:
            data=jwt.decode(token, app.config['SECRET_KEY'])
            current_user=User.query.filter_by(public_id=data['public_id']).first()
        except:
            return '<h1>Token is invalid</h1>',401
        return f(current_user, *args, **kwargs)
    
    return decorated


@app.route('/listuser',methods=['GET'])
def listuser():
     users=User_new.query.all()
    #  print("HII")
     return render_template("listUser.html",users=users)


@app.route('/register',methods=['POST','GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created {form.name.data}!','success')
        hashed_password=generate_password_hash(request.form['password'], method='sha256')
        new_user=User(public_id=str(uuid.uuid4()),name=request.form['name'],email=request.form['email'],password=hashed_password,admin=request.form['admin'])
        db.session.add(new_user)
        db.session.commit() 
        return redirect(url_for('index'))
    return render_template("register.html",form=form)



@app.route('/index')
def index():
    return render_template("index.html")

# @app.route('/adduser')
# def adduser():
#     countries=Countries.query.all()
#     states=States.query.all()
#     cities=Cities.query.all()
#     return render_template('adduser.html',countries=countries,states=states,cities=cities)


# @app.route('/')
# def login():
#      return render_template("login.html")


@app.route('/',methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        email=request.form['email']
        password=request.form['password']
        if not email or not password:
            return redirect(url_for('login'))
            
        user=User.query.filter_by(email=email).first()
        
        if not user:
            return redirect(url_for('login'))
            
        if check_password_hash(user.password, password):
            token = jwt.encode({'public_id':user.public_id, 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)} ,app.config['SECRET_KEY'])
            return redirect('/index')
        
        return redirect(url_for('login'))
    return render_template("login.html",form=form)





@app.route('/adduser',methods=['POST','GET'])
# @token_required
def adduser():
    # if not current_user.admin:
    #      return '<h1>Cannot perform that function</h1>'
    # form = UserForm()
    countries=Countries.query.all()
    states=States.query.all()
    cities=Cities.query.all()
   
    if request.method=='POST':
        user=User_new(name=request.form['name'],email=request.form['email'],mobile=request.form['mobile'],gender=request.form['gender'],country_id=request.form['country'],state_id=request.form['state'],city_id=request.form['city'],hobbies=request.form.getlist('hobbies[]'),address=request.form['address'])
        db.session.add(user)
        db.session.commit()
        return redirect('/listuser')
    return render_template('adduser.html',countries=countries,states=states,cities=cities)
   
    


@app.route('/states/<cid>',methods=['GET'])
def getstates(cid):
    states=States.query.filter_by(country_id=cid).all()
    return render_template('stateList.html',states=states)

@app.route('/cities/<cid>',methods=['GET'])
def getcities(cid):
    cities=Cities.query.filter_by(state_id=cid).all()
    return render_template('cityList.html',cities=cities)




@app.route('/edituser/<int:id>',methods=['POST','GET'])
def edituser(id):
    if request.method=='POST': 
        user=User_new.query.filter_by(id=id).first_or_404()
        # print("I'm put")
        user.name=request.form['name']
        user.email=request.form['email']
        user.mobile=request.form['mobile']
        user.gender=request.form['gender']
        user.country_id=request.form['country']
        user.state_id=request.form['state']
        user.city_id=request.form['city']
        user.hobbies=request.form.get('hobbies[]')
        user.address=request.form['address']
       
        # user=User_new(name=user.name,email= user.email,mobile= user.mobile,gender=user.gender,country=user.country,state=user.state,city=user.city,hobbies=user.hobbies,address=user.address)
        # db.session.add(user)
        db.session.commit()
        print("submitted")
        return redirect('/listuser')
    countries=Countries.query.all()
    states=States.query.all()
    cities=Cities.query.all()
    
    user=User_new.query.filter_by(id=id).first()
    # state=user.state_id
    # hobbies=int(user.hobbies)
    # print(state)
    return render_template("editUser.html",countries=countries,states=states,cities=cities,user=user)


@app.route('/deleteuser/<int:id>',methods=['GET','POST'])
def deleteuser(id):
        user=User_new.query.filter_by(id=id).first()
        # print("I'm delete")
        db.session.delete(user)
        db.session.commit()
        return redirect('/listuser')

@app.route("/sendmail")
def sendview():
    return render_template('sendMail.html')


@app.route("/send_mail",methods=['POST'])
def send():
   msg = Message('From ' + request.form['name'], sender = request.form['email'], recipients = ['kondapure1@gmail.com'])
   msg.body = request.form['message']
   mail.send(msg)
   return "Sent"