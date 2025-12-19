from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cinema-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cinema.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()
        seed_data()

    return app

def seed_data():
    from app.models import Movie, Session, Seat

    if Movie.query.first():
        return

    movies = [
        Movie(title="Interstellar"),
        Movie(title="Inception"),
        Movie(title="The Dark Knight"),
        Movie(title="Dune Part II")
    ]
    db.session.add_all(movies)
    db.session.commit()

    sessions = [
        Session(time="18:00", movie_id=movies[0].id),
        Session(time="21:00", movie_id=movies[0].id),
        Session(time="19:00", movie_id=movies[1].id),
        Session(time="22:00", movie_id=movies[2].id),
    ]
    db.session.add_all(sessions)

    seats = []
    for row in range(1, 6):
        for num in range(1, 9):
            seats.append(Seat(hall="Main Hall", row=row, number=num))

    db.session.add_all(seats)
    db.session.commit()
