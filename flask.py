import requests
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# Severe threat in production, but very common in local dev. The LLM should ask to be sure.
CORS(app, resources={r"/*": {"origins": "*"}})

def fetch_internal_data(api_url):
    # Disabling SSL verification. Is this a testing environment or a security flaw?
    response = requests.get(api_url, verify=False)
    return response.json()
