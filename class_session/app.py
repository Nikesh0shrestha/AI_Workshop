# app.py - Complete beginner-friendly Flask app

# 1. Import Flask
from flask import Flask, render_template, request


# dummy data 
# List of UI/UX topics from your BCA syllabus
topics = [
    {"id": 1, "name": "Fundamentals of UX and UI", "description": "Basic concepts of User Experience and User Interface design", "hours": 4},
    {"id": 2, "name": "UX vs UI", "description": "Differences between UX and UI designers and their roles", "hours": 2},
    {"id": 3, "name": "UX Principles", "description": "Usability, Accessibility, Simplicity", "hours": 3},
    {"id": 4, "name": "Core UX Disciplines", "description": "User research, IA, Interaction design, Visual design", "hours": 5},
    {"id": 5, "name": "User Interfaces Types", "description": "CLI, GUI, VUI, Menu-driven, NLP-based", "hours": 3},
]
# 2. Create the app
app = Flask(__name__)

# 3. Homepage route
@app.route('/')
def home():
    # This runs when someone visits /
    # return '''
    # <h1>📘 BCA UI/UX Notes</h1>
    # <p>Welcome to your study notebook server.</p>
    # <p>Try these links:</p>
    # <ul>
    #     <li><a href="/about">About this project</a></li>
    #     <li><a href="/user/student">Dynamic user page</a></li>
    # </ul>
    # '''
    return render_template('index.html')

# 4. About page
@app.route('/about')
def about():
    return '''
    <h1>About This Flask App</h1>
    <p>This app is part of your BCA UI/UX notebook.</p>
    <p>Flask helps you turn Python code into web pages.</p>
    <a href="/">← Back to Home</a>
    '''

# 5. Dynamic user page
@app.route('/user/<username>')
def user_profile(username):
    # Show different content based on the URL
    return f'''
    <h1>👤 User Profile: {username}</h1>
    <p>This page is personalized for {username}.</p>
    <p>In a real app, you would load data from a database here.</p>
    <a href="/">← Back to Home</a>
    '''


@app.route('/topics')
def topics_list():
    """Show all UI/UX topics"""
    # Pass the entire topics list to the template
    return render_template('/topics.html', title="Topics - UI/UX Syllabus", topics=topics)

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():

    # Get form data
    hours_studied = float(request.form['hours_studied'])
    previous_score = float(request.form['previous_score'])
    attendance = float(request.form['attendance'])
    sleep_hours = float(request.form['sleep_hours'])

    extracurricular = request.form['extracurricular']
    parent_education = request.form['parent_education']
    internet_access = request.form['internet_access']

    # Convert categorical values to numbers
    extracurricular_bonus = 5 if extracurricular == "Yes" else 0
    internet_bonus = 3 if internet_access == "Yes" else 0

    # Parent education bonus
    education_bonus = {
        "High School": 1,
        "Bachelor": 3,
        "Master": 5,
        "PhD": 7
    }

    parent_bonus = education_bonus.get(parent_education, 0)

    # Prediction Formula
    predicted_score = (
        hours_studied * 2.5 +
        previous_score * 0.5 +
        attendance * 0.3 +
        sleep_hours * 1.5 +
        extracurricular_bonus +
        internet_bonus +
        parent_bonus
    )

    # Keep score between 0 and 100
    predicted_score = max(0, min(100, predicted_score))

    return f"""
    <h1>Prediction Result</h1>

    <h2>Predicted Final Score: {predicted_score:.2f}</h2>

    <a href="/">Predict Another Student</a>
    """


# 6. Run the server
if __name__ == '__main__':
    # debug=True means: 
    # - Server restarts when you save code
    # - Shows error messages in browser (helpful for learning)
    app.run(debug=True)



    