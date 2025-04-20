from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # handle form submission
        name = request.form['name']
        email = request.form['email']
        # ... save to db or send confirmation
        return "Booking received!"
    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=True)
