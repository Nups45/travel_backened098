from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/hostel')
def hostel():
    return render_template('hostel_form.html')

@app.route('/pickup')
def pickup():
    return render_template('pickup_form.html')

# Optional: Remove if you don't have this template
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
