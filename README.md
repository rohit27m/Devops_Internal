# Weather Application - DevOps Lab Exercise

A Flask-based weather application that allows users to get real-time weather information for any city. This project demonstrates DevOps principles including containerization with Docker, version control with Git, and continuous integration practices.

## Project Structure

```
.
├── app.py              # Main Flask application with weather API integration
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker containerization file
├── static/             # Static assets
│   └── style.css       # CSS styling for the weather app
└── templates/          # HTML templates
    └── index.html      # Weather app template with search functionality
```

## Features

- Search for weather by city name
- Display current temperature, feels like, humidity, pressure, and wind speed
- Responsive design that works on mobile and desktop
- Server information display (hostname, Python version)
- Containerized application for consistent deployment

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Rohit27m/Devops_Internal.git
cd Devops_Internal
```

### 2. Get a Weatherstack API Key

1. Sign up at [Weatherstack](https://weatherstack.com/) to get a free API key
2. The API key will be used when running the application

### 3. Build and Run with Docker

Build the Docker image:

```bash
docker build -t weatherapp .
```

Run the Docker container:

```bash
# The API key is already set in the Docker image, but you can override it if needed
docker run -p 5001:5000 -d --name weatherapp-container weatherapp

# If you want to use your own API key:
docker run -p 5001:5000 -e WEATHERSTACK_API_KEY=your_api_key_here -d --name weatherapp-container weatherapp
```

Visit the application in your browser at http://localhost:5001

### 4. (Optional) Push to Docker Hub

Tag your Docker image:

```bash
docker tag weatherapp yourusername/weatherapp:latest
```

Push to Docker Hub:

```bash
docker login
docker push yourusername/weatherapp:latest
```

## Development

### Running Locally (Without Docker)

1. Set up a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/macOS
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your API key as an environment variable:
   ```bash
   $env:WEATHERSTACK_API_KEY="your_api_key_here"  # PowerShell
   ```

4. Run the application:
   ```bash
   python app.py
   ```

### Using VS Code Tasks

This project includes VS Code tasks to simplify development:

- `Install Dependencies`: Installs required Python packages
- `Run Flask App`: Runs the Flask app locally
- `Build Docker Image`: Builds the Docker image
- `Run Docker Container`: Runs the container with OpenWeatherMap API key
- `Build and Run Weather App`: Combines both Docker build and run
- `Stop and Remove Container`: Stops and removes the running container
- `Push to Docker Hub`: Tags and pushes the image to Docker Hub

## DevOps Best Practices Implemented

- **Docker Optimization**: Multi-stage build, slim base image, non-root user
- **Environment Configuration**: Using environment variables for API keys
- **Security**: Running container as non-root user
- **Version Control**: Project structured for Git with .gitignore
- **Documentation**: Comprehensive README and code comments
