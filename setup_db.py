from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

db = SQLAlchemy()
mongo = PyMongo()

class User(db.Model):
    __tablename__ = 'users'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Email = db.Column(db.String(255), primary_key=True)
    Password = db.Column(db.String(255))

class Email:
    def __init__(self, ID:int, Sender:str, Recipient:str, Subject:str, Body:str, Date:str, Time:str, Email_id:int):
        self.ID = ID
        self.Sender = Sender
        self.Recipient = Recipient
        self.Subject = Subject
        self.Body = Body
        self.Date = Date
        self.Time = Time
        self.Email_id = Email_id

class Summary:
    def __init__(self, ID:int, Email_id:int, Summary_text:str, Date:str):
        self.ID = ID
        self.Email_id = Email_id
        self.Summary_text = Summary_text
        self.Date = Date

class Responses(db.Model):
    __tablename__ = 'responses'
    ID = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('users.ID'))
    Response_text = db.Column(db.String(255))
    Keywords = db.Column(db.String(255))

class DatabaseSetup:
    def __init__(self, db_uri:str, mongo_uri:str):
        self.db_uri = db_uri
        self.mongo_uri = mongo_uri
        self.db = SQLAlchemy()
        self.mongo = PyMongo()
        
    def create_all(self):
        self.db.init_app(self.db_uri)
        self.mongo.init_app(self.mongo_uri)
        self.db.create_all()
        self.mongo.db.email.create_index([("id", 1)], unique=True)
        self.mongo.db.summary.create_index([("id", 1)], unique=True)

