from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travelapp.db'
db = SQLAlchemy(app)

# Destination model
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country = db.Column(db.String(100))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))

# Create tables
with app.app_context():
    db.create_all()
# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Add a new destination
@app.route('/add-destination', methods=['POST'])
def add_destination():
    data = request.json
    new_dest = Destination(
        name=data['name'],
        country=data['country'],
        description=data['description'],
        image_url=data['image_url']
    )
    db.session.add(new_dest)
    db.session.commit()
    return jsonify({'message': 'Destination added successfully'})
# Get all destinations
@app.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    result = []
    for dest in destinations:
        result.append({
            'id': dest.id,
            'name': dest.name,
            'country': dest.country,
            'description': dest.description,
            'image_url': dest.image_url
        })
    return jsonify(result)

if _name_ == '_main_':
    app.run(debug=True)

