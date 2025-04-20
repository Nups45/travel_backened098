from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TicketBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    date = db.Column(db.String(20))

class HostelBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    checkin = db.Column(db.String(20))
    checkout = db.Column(db.String(20))

class PickupService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    pickup = db.Column(db.String(100))
    drop = db.Column(db.String(100))
    time = db.Column(db.String(10))
