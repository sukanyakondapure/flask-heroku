from app import db

class User(db.Model):    #for registration page
    id = db.Column(db.Integer, primary_key=True)
    public_id=db.Column(db.String(50), unique=True)
    name= db.Column(db.String(50))   
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(80))
    admin=db.Column(db.String(11))

class User_new(db.Model):  
    __tablename__ = 'user_new'  
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50))   
    email=db.Column(db.String(50),unique=True)
    mobile= db.Column(db.Integer) 
    country_id=db.Column(db.Integer,db.ForeignKey('country.id'))
    state_id=db.Column(db.Integer,db.ForeignKey('state.id'))
    city_id=db.Column(db.Integer,db.ForeignKey('city.id'))
    gender=db.Column(db.Integer)
    hobbies=db.Column(db.String(100))
    address=db.Column(db.String(255))
    countryname = db.relationship('Countries', backref=db.backref('user_new'))
    statename = db.relationship('States', backref=db.backref('user_new'))
    cityname = db.relationship('Cities', backref=db.backref('user_new'))


    def __init__(self,name,email,mobile,country_id,state_id,city_id,gender,hobbies,address):

        self.name=name
        self.email=email
        self.mobile=mobile
        self.country_id=country_id
        self.state_id=state_id
        self.city_id=city_id
        self.gender=gender
        self.hobbies=hobbies
        self.address=address
        
    


class Countries(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50)) 

class States(db.Model):
    __tablename__ = 'state'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50)) 
    country_id=db.Column(db.Integer)

class Cities(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50)) 
    state_id=db.Column(db.Integer)


class FileContents(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(300))
    data=db.Column(db.LargeBinary)