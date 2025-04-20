from flask import Flask, render_template

app = Flask(__name__)

# ✅ This is the key route you're missing
@app.route('/bookings')
def show_all_bookings():
    return render_template('all_bookings.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)

