from flask import Flask, render_template, request
from markupsafe import Markup
from generator import generate_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    keyword = request.form["keyword"]
    generated_text = generate_text(keyword)
    generated_text = Markup(generated_text)
    return render_template("index.html", generated_text=generated_text)

if __name__ == '__main__':
    app.run()