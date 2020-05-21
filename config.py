from app import app 

DEBUG=  True
app.config['SECRET_KEY']='thisissecret'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'cda9c0ba5f92fb'
app.config['MAIL_PASSWORD'] = '36e1e46062b5ca'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['DATABASE_URL']='postgres://pwnalsqrkxfley:70ce524161968897a83698615e3947642097eca05d38a5efed17484182f22b63@ec2-52-7-39-178.compute-1.amazonaws.com:5432/ddv61sirqu5k8h'


