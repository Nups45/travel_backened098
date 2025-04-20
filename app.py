from flask import Flask, render_template, request, redirect
from models import db, TicketBooking, HostelBooking, PickupService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travelapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create DB Tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/book', methods=['GET', 'POST'])
def book_ticket():
    if request.method == 'POST':
        data = TicketBooking(
            name=request.form['name'],
            email=request.form['email'],
            destination=request.form['destination'],
            date=request.form['date']
        )
        db.session.add(data)
        db.session.commit()
        return render_template('confirmation.html', type='Ticket', data=data)
    return render_template('book_form.html')

@app.route('/hostel', methods=['GET', 'POST'])
def hostel_service():
    if request.method == 'POST':
        data = HostelBooking(
            name=request.form['name'],
            location=request.form['location'],
            checkin=request.form['checkin'],
            checkout=request.form['checkout']
        )
        db.session.add(data)
        db.session.commit()
        return "Hostel booked successfully!"
    return render_template('hostel_form.html')

@app.route('/pickup', methods=['GET', 'POST'])
def pickup_service():
    if request.method == 'POST':
        data = PickupService(
            name=request.form['name'],
            pickup=request.form['pickup'],
            drop=request.form['drop'],
            time=request.form['time']
        )
        
   
        db.session.commit()
        return "Pickup scheduled successfully!"
    return render_template('pickup_form.html')

if __name__ == '__main__':
    app.run(debug=True)
