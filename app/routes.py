from flask import Blueprint, render_template, request
from app.models import Booking
from app.app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/book', methods=['POST'])
def book():
    booking = Booking(
        movie=request.form['movie'],
        session=request.form['session'],
        hall=request.form['hall'],
        row=request.form['row'],
        seat=request.form['seat'],
        customer_name=request.form['customer_name']
    )
    db.session.add(booking)
    db.session.commit()
    return render_template('success.html', booking=booking)
