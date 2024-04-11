from flask import Flask, render_template, request
from main import generate_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main.py', methods=['POST'])
def generate_text_route():
    try:
        length = int(request.form['length'])  # Get length from form input
        temperature = float(request.form['temperature'])  # Get temperature from form input
        generated_text = generate_text(length, temperature)  # Call generate_text function with input parameters from main.py
        return render_template('index.html', generated_text=generated_text, error_message=None)  # Pass generated text to template
    except Exception as e:
        error_message = str(e)  # Get the error message
        return render_template('index.html', generated_text=None, error_message=error_message)  # Pass error message to template

if __name__ == '__main__':
    app.run(debug=True)