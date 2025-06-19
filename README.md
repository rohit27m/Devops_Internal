# DevOps Lab Exercise

A simple Flask web application that displays a welcome message, containerized using Docker.

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker containerization file
├── static/             # Static assets
│   └── style.css       # CSS styling
└── templates/          # HTML templates
    └── index.html      # Main page template
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd <repository-name>
```

### 2. Modify the Code

Change the welcome message in `app.py` and `templates/index.html` to:
"Hello from <Your Full Name>!"

Save, commit, and push the changes to your GitHub repository:

```bash
git add .
git commit -m "Update welcome message"
git push origin main
```

### 3. Build and Run with Docker

Build the Docker image:

```bash
docker build -t myapp .
```

Run the Docker container:

```bash
docker run -p 5000:5000 myapp
```

Visit the application in your browser at http://localhost:5000

### 4. (Optional) Push to Docker Hub

Tag your Docker image:

```bash
docker tag myapp yourusername/myapp
```

Push to Docker Hub:

```bash
docker login
docker push yourusername/myapp
```

## Submission

1. Submit your GitHub repository link containing all the files: code, Dockerfile, and this README.
2. Include documentation on how you completed each step of the assignment.

## Documentation

(Add your documentation here for how you completed each step of the assignment)
