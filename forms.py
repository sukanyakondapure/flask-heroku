from flask_wtf import FlaskForm
from app import db
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,IntegerField,RadioField,SelectField,BooleanField
from wtforms.validators import DataRequired,Length,Email
from models import Countries,States,Cities

class RegistrationForm(FlaskForm):
   name = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
   email=StringField('Email', validators=[DataRequired(),Email()])
   password=PasswordField('Password',validators=[DataRequired()])
   submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
   email=StringField('Email', validators=[DataRequired(),Email()])
   password=PasswordField('Password',validators=[DataRequired()])
   submit=SubmitField('Login')

class UserForm(FlaskForm):
   countries=Countries.query.all()
   states=States.query.all()
   cities=Cities.query.all()
   countryArray=[]
   stateArray=[]
   cityArray=[]
   for country in countries:
      countryobj={}
      countryobj['id']=country.id
      countryobj['name']=country.name
      countryArray.append(countryobj)
   for state in states:
      stateobj={}
      stateobj['id']=state.id
      stateobj['name']=state.name
      stateArray.append(stateobj)
   for city in cities:
      cityobj={}
      cityobj['id']=city.id
      cityobj['name']=city.name
      cityArray.append(cityobj)

   
   name = StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
   email=StringField('Email', validators=[DataRequired(),Email(),Length(min=2,max=50)])
   mobile=IntegerField('Mobile', validators=[DataRequired(),Length(max=11)])
   country=SelectField('Country', validators=[DataRequired()], coerce=int, choices=countryArray)
   state=SelectField('State',validators=[DataRequired()], coerce=int,choices=stateArray)
   city=SelectField('City',validators=[DataRequired()], coerce=int,choices=cityArray)
   gender=RadioField('Gender', choices = [('M','Male'),('F','Female')])
   hobbies=BooleanField('Hobbies',validators=[DataRequired()])
   address=TextAreaField('address',validators=[DataRequired()])
   submit=SubmitField('Submit')
  
