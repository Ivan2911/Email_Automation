from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from setup_db import DatabaseSetup
import imaplib
import email

# Create a Flask app
app = Flask(__name__)

# Define a route for the index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Get user information from the request
    user_info = request.get_json()

    setup = DatabaseSetup('mysql://username:password@host:port/dbname', 'mongodb://username:password@host:port/dbname')
    setup.create_all()

    # Create a new user object
    new_user = User(name=user_info['name'], email=user_info['email'], password=user_info['password'])

    # Add the new user to the session
    db.session.add(new_user)

    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201
# Run the app
if __name__ == '__main__':
    app.run(port=8000)

