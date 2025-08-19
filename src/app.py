"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball training and inter-school matches",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["alex@mergington.edu", "jamie@mergington.edu"]
    },
    "Soccer Club": {
        "description": "Soccer practice and friendly matches with other schools",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["carlos@mergington.edu", "maya@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore various art mediums including painting, drawing, and sculpture",
        "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["lily@mergington.edu", "noah@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting workshops and theatrical performances",
        "schedule": "Fridays, 3:00 PM - 6:00 PM",
        "max_participants": 25,
        "participants": ["grace@mergington.edu", "ethan@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop critical thinking and public speaking through competitive debates",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["ava@mergington.edu", "william@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "Competitive science events covering biology, chemistry, physics, and engineering",
        "schedule": "Saturdays, 10:00 AM - 12:00 PM",
        "max_participants": 18,
        "participants": ["zoe@mergington.edu", "lucas@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
