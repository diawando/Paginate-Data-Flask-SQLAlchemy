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
    page = request.args.get('page', 1, type=int)
    pagination = Employee.query.order_by(Employee.firstname).paginate(page=page, per_page=2, error_out=False)
    return render_template('index.html', pagination=pagination)