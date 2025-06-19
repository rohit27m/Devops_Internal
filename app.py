from flask import Flask, render_template
import datetime
import platform
import socket
import sys

app = Flask(__name__)

@app.route('/')
def index():
    # Get current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get hostname
    hostname = socket.gethostname()
    
    # Get Python version
    python_version = sys.version
    
    return render_template('index.html', 
                          name="Rohit Munamarthi",
                          current_time=current_time,
                          hostname=hostname,
                          python_version=python_version)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
