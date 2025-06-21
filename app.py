from flask import Flask, render_template, request
import datetime
import platform
import socket
import sys
import os
import requests

app = Flask(__name__)

# Weatherstack API key - in production, use environment variables
# For demo purposes, we'll use a provided key
API_KEY = os.environ.get('WEATHERSTACK_API_KEY', '16a8978c55399e1ea24075eec49ba8d5')
API_URL = "http://api.weatherstack.com/current"

@app.route('/', methods=['GET', 'POST'])
def index():
    # Get current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get hostname
    hostname = socket.gethostname()
    
    # Get Python version
    python_version = sys.version
    
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            try:
                # Make API request to Weatherstack
                params = {
                    'access_key': API_KEY,
                    'query': city,
                    'units': 'm'  # For temperature in Celsius
                }
                
                response = requests.get(API_URL, params=params)
                response.raise_for_status()  # Raise exception for HTTP errors
                
                data = response.json()
                
                # Process weather data from Weatherstack format
                if data.get('success', True) == False:
                    error = f"API Error: {data.get('error', {}).get('info', 'Unknown error')}"
                    raise ValueError(error)
                
                weather_data = {
                    'city': data['location']['name'],
                    'country': data['location']['country'],
                    'temperature': data['current']['temperature'],
                    'feels_like': data['current']['feelslike'],
                    'description': data['current']['weather_descriptions'][0],
                    'icon_url': data['current']['weather_icons'][0],
                    'humidity': data['current']['humidity'],
                    'pressure': data['current']['pressure'],
                    'wind_speed': data['current']['wind_speed']
                }
            except requests.exceptions.RequestException as e:
                error = f"Error fetching weather data: {str(e)}"
            except (KeyError, ValueError) as e:
                error = f"Error processing weather data: {str(e)}"
    
    return render_template('index.html', 
                          name="Rohit Munamarthi, Rithvik Myneni and R.V.K.S.N. Raju",
                          current_time=current_time,
                          hostname=hostname,
                          python_version=python_version,
                          weather_data=weather_data,
                          error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
