from flask import Flask, request, render_template
import qrcode
import os

app = Flask(__name__)

@app.route("/")
def index():
    if os.path.exists('static/qrcode.png'):
        os.remove('static/qrcode.png')
    return render_template('index.html', qr="")

@app.route("/generate")
def generate():
    img = qrcode.make(request.args.get('data', ''))
    img.save('static/qrcode.png', 'PNG')
    return render_template('index.html', qr="../static/qrcode.png")