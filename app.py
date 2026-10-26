"""
Arpit Turukmare - Portfolio Website
Flask application for DevOps Lab Practical
Pipeline: GitHub → Jenkins → pytest → Docker → Kubernetes → AWS EC2
"""

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Homepage - About Me"""
    return render_template("index.html", active_page="home")


@app.route("/projects")
def projects():
    """Projects page - showcasing all projects"""
    return render_template("projects.html", active_page="projects")


@app.route("/skills")
def skills():
    """Skills page - technical skills"""
    return render_template("skills.html", active_page="skills")


@app.route("/achievements")
def achievements():
    """Achievements page - hackathons, certifications"""
    return render_template("achievements.html", active_page="achievements")


@app.route("/health")
def health():
    """Health check endpoint for monitoring"""
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
