from flask_restful import Resource,reqparse,Api
from app import db
from flask import Flask,render_template,request,jsonify
from models import User_new


parser = reqparse.RequestParser()
class User(Resource):
    def get(self):
        users_list = User_new.query.all()
        users=[]
        
        for user in users_list:
            users.append({
                'id':user.id,
                'name':user.name,
                'email':user.email,
                'mobile':user.mobile,
                'country_id':user.country_id,
                'state_id':user.state_id,
                'city_id':user.city_id,
                'gender':user.gender,
                'address':user.address
    
            })
            return jsonify({'Users':users})


    def post(self):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('mobile', type=int)
        parser.add_argument('country_id', type=int)
        parser.add_argument('state_id', type=int)
        parser.add_argument('city_id', type=int)  
        parser.add_argument('gender', type=str)
        parser.add_argument('hobbies', type=str)
        parser.add_argument('address', type=str)
        args=parser.parse_args()
   
       
        user=User_new(args['name'],args['email'],args['mobile'],args['country_id'],args['state_id'],args['city_id'],args['gender'],args['hobbies'],args['address'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message':'User created'})

class User_modify(Resource):
    def put(self,id):
        
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('mobile', type=int)
        parser.add_argument('country_id', type=int)
        parser.add_argument('state_id', type=int)
        parser.add_argument('city_id', type=int)  
        parser.add_argument('gender', type=str)
        parser.add_argument('hobbies', type=str)
        parser.add_argument('address', type=str)

        args=parser.parse_args()
        User_new.query.filter_by(id=id).update({'name':args['name'],'email':args['email'],'mobile':args['mobile'],
        'country_id':args['country_id'],'state_id':args['state_id'],'city_id':args['city_id'],'gender':args['gender'],'hobbies':args['hobbies'],'address':args['address']
          })

       
        db.session.commit()
        return jsonify({'message':'User updated'})
    
    def delete(self,id):
        user=User_new.query.filter_by(id=id).first_or_404()
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message':'User deleted'})



    
    

  
       


 
  