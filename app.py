from flask import Flask, send_file, jsonify
import os
import random
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/cart.json')
def cart():
    return jsonify({'cart': []})

@app.route('/send_file')
def send_file():
    # Create a file with random contents
    with open('file.txt', 'w') as f:
        f.write(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=1024)))

    # Calculate the checksum of the file
    with open('file.txt', 'rb') as f:
        checksum = hashlib.md5(f.read()).hexdigest()

    # Send the file contents and checksum to the client
    return send_file('file.txt'), {'Checksum': checksum}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
