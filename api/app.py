"""
Flask application to host the APIs that we plan to use for Tally AI
"""
import requests
import json

from flask import Flask, render_template
from flask_cors import CORS
from decouple import config

def create_app():
    """
    Web app for API endpoints
    """

    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def home():
        """
        Documents endpoints for all APIs. Currently just Yelp 
        """
        return render_template('index.html')
    
    @app.route("/<business_id>", methods=['GET', 'POST'])
    def yelp(business_id):
        """ 
        Endpoint for Yelp API. Requires business_id to retrieve info.
        """
        API_KEY = config('YELP_API_KEY')
        HEADERS = {'Authorization': f'Bearer {API_KEY}'}
        
        BUSINESS_ID = business_id
        URL = f'https://api.yelp.com/v3/businesses/{BUSINESS_ID}/reviews'

        req = requests.get(URL, headers=HEADERS)
        parsed = json.loads(req.text)
        reviews = parsed['reviews']

        reviews_json = []
        for review in reviews:
            reviews_json.append(review)
        
        result = json.dumps(reviews_json, indent=2)

        return result
    
    return app