# server.py
from flask import Flask, request, jsonify, render_template
from pyngrok import ngrok
from threading import Thread

app = Flask(__name__)
locations = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map_view():
    return render_template('map.html')

@app.route('/location', methods=['POST'])
def receive_location():
    data = request.json
    locations.append(data)
    return jsonify(status="ok")

@app.route('/locations')
def send_locations():
    return jsonify(locations)

def start_ngrok():
    url = ngrok.connect(5000)
    print(f"[+] Public URL: {url}")
    print(f"[+] Map Dashboard: {url}/map")

if __name__ == '__main__':
    Thread(target=start_ngrok).start()
    app.run(host="0.0.0.0", port=5000)
