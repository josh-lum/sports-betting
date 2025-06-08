from app import db

# Define Bet model for storing odds data in the database
class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(100))
    odds = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)