import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lavie@localhost:5432/entreprise'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return f'<Employee {self.firstname} {self.lastname}>'
    
    

@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)