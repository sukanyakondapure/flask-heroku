from models import FileContents
from app import db
from flask_restful import Resource
from flask import Flask,render_template,make_response,request,redirect,url_for,send_file,flash
from io import BytesIO

class Uploadfile(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('upload.html'),200,headers)
    
    def post(self):
        headers = {'Content-Type': 'text/html'}
        file = request.files['inputFile']
        newfile=FileContents(name=file.filename,data=file.read())
        db.session.add(newfile)
        db.session.commit()
        # flash("Saved to database")
        #   f.save(secure_filename(f.filename))
        return make_response(render_template('upload.html'),200,headers)

class Downloadfile(Resource):
    def post(self):
        file_data=FileContents.query.filter_by(id=13).first()
        return send_file(BytesIO(file_data.data),attachment_filename='downloaded_file.xlsx' ,as_attachment=True)
