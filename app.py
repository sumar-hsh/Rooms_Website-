from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'jkbksxkxanlmljolkax'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rooms.db'
db = SQLAlchemy(app)


# Define a list of users to ad
# Room model
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    has_bathroom = db.Column(db.Boolean, default=False)
    has_balcony = db.Column(db.Boolean, default=False)
    has_window = db.Column(db.Boolean, default=False)
    is_partition = db.Column(db.Boolean, default=False)
    region = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)


def add_rooms():
    # Only add rooms if the table is empty
    if Room.query.count() == 0:
        room1 = Room(title='Комната в Дубай Марина', price=1500, rating=4.5, has_bathroom=True,
                     has_balcony=True, has_window=True, is_partition=False, region='Dubai Marina',
                     image_url='static/images/room1.jpg', location='Dubai Marina, Street 1')

        room2 = Room(title='Комната в Центре Дубая', price=1800, rating=4.7, has_bathroom=True,
                     has_balcony=False, has_window=True, is_partition=True, region='Downtown Dubai',
                     image_url='static/images/room2.jpg', location='Downtown Dubai, Street 2')

        # Add the rooms to the session
        db.session.add(room1)
        db.session.add(room2)
        db.session.commit()

# Create the database and add initial data
def create_tables():
    with app.app_context():  # This ensures the application context is active
        db.create_all()
        add_rooms()


# Home route
@app.route('/')
def index():
    rooms = Room.query.all()
    return render_template('index.html', rooms=rooms)

if __name__ == '__main__':
    create_tables()  # Ensure tables and initial data are created
    app.run(debug=True)
