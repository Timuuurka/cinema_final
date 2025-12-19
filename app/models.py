from app.app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    movie = db.relationship('Movie', backref=db.backref('sessions', lazy=True))

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hall = db.Column(db.String(20), nullable=False)
    row = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('session_id', 'seat_id', name='unique_seat_booking'),
    )

    session = db.relationship('Session')
    seat = db.relationship('Seat')
