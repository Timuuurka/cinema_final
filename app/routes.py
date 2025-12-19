from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Movie, Session, Seat, Booking
from app.app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@main.route('/sessions/<int:movie_id>')
def sessions(movie_id):
    sessions = Session.query.filter_by(movie_id=movie_id).all()
    return render_template('sessions.html', sessions=sessions)

@main.route('/seats/<int:session_id>')
def seats(session_id):
    all_seats = Seat.query.all()
    booked = {b.seat_id for b in Booking.query.filter_by(session_id=session_id).all()}
    available = len(all_seats) - len(booked)
    return render_template(
        'seats.html',
        seats=all_seats,
        booked=booked,
        session_id=session_id,
        available=available
    )

@main.route('/book', methods=['POST'])
def book():
    session_id = request.form['session_id']
    seat_id = request.form['seat_id']
    name = request.form['name']

    booking = Booking(
        session_id=session_id,
        seat_id=seat_id,
        customer_name=name
    )

    db.session.add(booking)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return "Seat already booked", 400

    return redirect(url_for('main.index'))
