from flask import Flask
# import the flask class from Flask
from flask_sqlalchemy import SQLAlchemy
# helps to link to the flask app and begin using sqlalchemy

app = Flask(__name__)
# instantiate the app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///example'
# connect to db from flask app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# links an instance of a database that can be interacted with using SQLAlchemy to the flask app

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

  def __repr__(self):
    # dunder method to change the output format
    return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

@app.route('/')
# @app - python decorator
# .route('/') - tells the app to listen to the homepage route for connections

def index():
    # route handler index listens to the route route and determines what to do next
    person = Person.query.first() 
    # retrieves the first record inside the Persons table
    return 'Hello ' + person.name