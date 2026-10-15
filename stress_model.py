"""
Academic Stress Prediction Model
Predicts a student's academic stress level (Low / Medium / High) with a
Decision Tree classifier and generates a personalised study plan.
"""

import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# -----------------------------

# 1. DATASET CREATION

# -----------------------------

np.random.seed(42)

rows = 300

data = {

    "Subjects": np.random.randint(3, 8, rows),

    "Tasks": np.random.randint(4, 12, rows),

    "Difficulty": np.random.randint(1, 6, rows),

    "Deadlines": np.random.randint(1, 14, rows),

    "StudyHours": np.random.randint(1, 7, rows),

    "Sleep": np.random.randint(4, 9, rows),

    "ExamDays": np.random.randint(1, 21, rows)

}

df = pd.DataFrame(data)

# Stress labeling logic

def assign_stress(row):

    score = (

        row['Tasks'] * 0.3 +

        row['Difficulty'] * 0.4 -

        row['StudyHours'] * 0.5 -

        row['Sleep'] * 0.3 +

        (14 - row['Deadlines']) * 0.2

    )

    if score > 6:

        return "High"

    elif score > 3:

        return "Medium"

    else:

        return "Low"

df['StressLevel'] = df.apply(assign_stress, axis=1)

# -----------------------------

# 2. MODEL TRAINING

# -----------------------------

X = df.drop('StressLevel', axis=1)

y = df['StressLevel']

X_train, X_test, y_train, y_test = train_test_split(

    X, y, test_size=0.2, random_state=42

)

model = DecisionTreeClassifier(max_depth=5, random_state=42)

model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model accuracy on test set: {accuracy:.2%}")

# -----------------------------

# 3. STUDY PLAN GENERATOR

# -----------------------------

def generate_study_plan(stress_level, student_data):

    plan = {}

    if stress_level == "High":

        plan['Priority'] = "Critical"

        plan['Recommendations'] = [

            "Break tasks into small daily goals",

            "Focus on nearest deadlines first",

            "Increase study time gradually",

            "Ensure at least 7 hours of sleep"

        ]

    elif stress_level == "Medium":

        plan['Priority'] = "Moderate"

        plan['Recommendations'] = [

            "Use Pomodoro technique",

            "Allocate more time to difficult subjects",

            "Maintain consistent study schedule"

        ]

    else:

        plan['Priority'] = "Low"

        plan['Recommendations'] = [

            "Maintain current routine",

            "Revise topics weekly",

            "Avoid overloading yourself"

        ]

    return plan

# -----------------------------

# 4. FULL PIPELINE FUNCTION

# -----------------------------

def stress_prediction_pipeline(student_input):

    input_df = pd.DataFrame([student_input])

    stress_level = model.predict(input_df)[0]

    study_plan = generate_study_plan(stress_level, student_input)

    return stress_level, study_plan

# -----------------------------

# 5. TEST THE COMPLETE SYSTEM

# -----------------------------

student_input = {

    "Subjects": 5,

    "Tasks": 9,

    "Difficulty": 4,

    "Deadlines": 3,

    "StudyHours": 2,

    "Sleep": 5,

    "ExamDays": 7

}

predicted_stress, plan = stress_prediction_pipeline(student_input)

print("Predicted Stress Level:", predicted_stress)

print("\nPersonalized Study Plan:")

for tip in plan['Recommendations']:

    print("-", tip)
