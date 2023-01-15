from flask import Flask, render_template, request, redirect


# Create a Flask app
app = Flask(__name__)

# Define a route for the index page
@app.route('/')
def index():
    return render_template('summary.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8000)

