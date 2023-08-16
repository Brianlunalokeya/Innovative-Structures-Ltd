from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Clients Table
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    industry = db.Column(db.String(100))
    projects = db.relationship('Project', backref='client', lazy=True)

# Projects Table
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    team_members = db.relationship('TeamMember', secondary='project_team', backref='projects', lazy=True)
    services = db.relationship('Service', secondary='project_service', backref='projects', lazy=True)

# Team Members Table
class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)
    image_url = db.Column(db.String(200))

# Services Table
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

# Project-Team Association Table
project_team = db.Table('project_team',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('team_member_id', db.Integer, db.ForeignKey('team_member.id'), primary_key=True)
)

# Project-Service Association Table
project_service = db.Table('project_service',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'), primary_key=True)
)
