from app.app import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(100), nullable=False)
    session = db.Column(db.String(50), nullable=False)
    hall = db.Column(db.String(20), nullable=False)
    row = db.Column(db.Integer, nullable=False)
    seat = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Booking {self.movie} Seat {self.row}-{self.seat}>"
