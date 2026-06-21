from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model/career_model.pkl")

# Career Information
career_info = {
    "Software Engineer": {
        "description": "Designs and develops software applications, websites, and mobile apps.",
        "salary": "₹4 LPA - ₹15 LPA",
        "skills": ["Python", "Java", "Problem Solving", "Data Structures"]
    },

    "Data Scientist": {
        "description": "Analyzes data and builds machine learning models.",
        "salary": "₹6 LPA - ₹20 LPA",
        "skills": ["Python", "Statistics", "Machine Learning", "SQL"]
    },

    "Marketing Manager": {
        "description": "Plans marketing strategies and promotes products.",
        "salary": "₹5 LPA - ₹18 LPA",
        "skills": ["Communication", "Leadership", "Marketing", "Creativity"]
    },

    "Graphic Designer": {
        "description": "Creates visual content and digital designs.",
        "salary": "₹3 LPA - ₹10 LPA",
        "skills": ["Photoshop", "Creativity", "UI Design", "Illustrator"]
    },

    "Teacher": {
        "description": "Educates and guides students.",
        "salary": "₹3 LPA - ₹8 LPA",
        "skills": ["Communication", "Leadership", "Subject Knowledge"]
    }
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    maths = int(request.form['maths'])
    programming = int(request.form['programming'])
    communication = int(request.form['communication'])
    creativity = int(request.form['creativity'])
    leadership = int(request.form['leadership'])

    features = np.array([[
        maths,
        programming,
        communication,
        creativity,
        leadership
    ]])

    prediction = model.predict(features)[0]

    # Default values if career not found
    info = career_info.get(
        prediction,
        {
            "description": "No description available.",
            "salary": "Not Available",
            "skills": ["Skill information unavailable"]
        }
    )

    suggestions = []

    if communication < 60:
        suggestions.append(
            "Improve presentation and public speaking skills."
        )

    if programming < 60:
        suggestions.append(
            "Practice coding regularly and build mini projects."
        )

    if maths < 60:
        suggestions.append(
            "Improve analytical and mathematical problem-solving skills."
        )

    if creativity < 60:
        suggestions.append(
            "Work on creative projects and brainstorming activities."
        )

    if leadership < 60:
        suggestions.append(
            "Participate in team activities and leadership roles."
        )

    if len(suggestions) == 0:
        suggestions.append(
            "Excellent skill profile. Continue improving your strengths."
        )

    return render_template(
        'result.html',
        career=prediction,
        description=info["description"],
        salary=info["salary"],
        skills=info["skills"],
        suggestions=suggestions
    )


if __name__ == "__main__":
    app.run(debug=True)