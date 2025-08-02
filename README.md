# 📍 Live Location Tracker (Ethical Testing Tool)

This project captures and visualizes a user's **live location** after they give permission. It is built for **educational, ethical hacking, and testing purposes only**.

---

## 🚀 Features

- 🌐 Publicly accessible via Ngrok (HTTPS support)
- 📍 HTML5 Geolocation API support
- 🗺️ Live map display using Leaflet.js
- 📡 Dual-view: Victim sees their own location + you see it live
- 📱 Mobile & desktop browser compatible

---

## ⚠️ Legal Disclaimer

This tool is for **educational and ethical use only**.  
⚠️ **DO NOT** use it without **explicit, informed consent** of the user you're tracking.  
Misuse of this tool may violate privacy laws and result in serious legal consequences.

---

## 🔧 Prerequisites

- Python 3
- pip3
- Ngrok (for HTTPS tunneling)
- flask

---

## 🐍 Python Setup

```bash
git clone https://github.com/yourusername/live-location-tracker
cd live-location-tracker
pip install -r requirements.txt
🌐 Ngrok Setup (Required for Public Access)
Browsers require HTTPS for geolocation to work. Ngrok gives you a secure HTTPS tunnel to your local server.

1. Install Ngrok
If you haven't already:

bash
Copy
Edit
# For Linux/Mac
brew install ngrok

# Or download manually from:
https://ngrok.com/download
2. Authenticate Ngrok (only once)
Sign up at ngrok.com, then:

bash
Copy
Edit
ngrok config add-authtoken <your_token>
3. Run the server (Ngrok launches automatically)
bash
Copy
Edit
python server.py
Ngrok will print a public HTTPS URL like:

less
Copy
Edit
[+] Public URL: https://abc123.ngrok.io
[+] Map Dashboard: https://abc123.ngrok.io/map
🔗 Usage
Send the Ngrok URL (e.g., https://abc123.ngrok.io) to your test target (they must give permission).

Once they click "Find Out Now" and allow location access, they’ll be redirected to /map.

You can watch live location updates at https://abc123.ngrok.io/map.
