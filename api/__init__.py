from flask_restful import Api
from app import app
from .User import User,User_modify
from .Quotes import Quotes
from .Uploadfile import Uploadfile,Downloadfile


restServer=Api(app)

restServer.add_resource(User , '/user')
restServer.add_resource(User_modify , '/edituser/<int:id>','/deleteuser/<int:id>')
restServer.add_resource(Quotes, '/api/quote', '/api/quote/update/<int:id>')
restServer.add_resource(Uploadfile, '/uploadfile')
restServer.add_resource(Downloadfile, '/download')