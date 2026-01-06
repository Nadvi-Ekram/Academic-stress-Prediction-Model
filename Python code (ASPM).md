

### **# Academic Stress Prediction Model**



import pandas as pd

import numpy as np

from sklearn.model\_selection import train\_test\_split

from sklearn.tree import DecisionTreeClassifier



\# -----------------------------

\# 1. DATASET CREATION

\# -----------------------------

np.random.seed(42)

rows = 300



data = {

&nbsp;   "Subjects": np.random.randint(3, 8, rows),

&nbsp;   "Tasks": np.random.randint(4, 12, rows),

&nbsp;   "Difficulty": np.random.randint(1, 6, rows),

&nbsp;   "Deadlines": np.random.randint(1, 14, rows),

&nbsp;   "StudyHours": np.random.randint(1, 7, rows),

&nbsp;   "Sleep": np.random.randint(4, 9, rows),

&nbsp;   "ExamDays": np.random.randint(1, 21, rows)

}



df = pd.DataFrame(data)



\# Stress labeling logic



def assign\_stress(row):

&nbsp;   score = (

&nbsp;       row\['Tasks'] \* 0.3 +

&nbsp;       row\['Difficulty'] \* 0.4 -

&nbsp;       row\['StudyHours'] \* 0.5 -

&nbsp;       row\['Sleep'] \* 0.3 +

&nbsp;       (14 - row\['Deadlines']) \* 0.2

&nbsp;   )

&nbsp;   if score > 6:

&nbsp;       return "High"

&nbsp;   elif score > 3:

&nbsp;       return "Medium"

&nbsp;   else:

&nbsp;       return "Low"





df\['StressLevel'] = df.apply(assign\_stress, axis=1)



\# -----------------------------

\# 2. MODEL TRAINING

\# -----------------------------

X = df.drop('StressLevel', axis=1)

y = df\['StressLevel']



X\_train, X\_test, y\_train, y\_test = train\_test\_split(

&nbsp;   X, y, test\_size=0.2, random\_state=42

)



model = DecisionTreeClassifier(max\_depth=5, random\_state=42)

model.fit(X\_train, y\_train)



\# -----------------------------

\# 3. STUDY PLAN GENERATOR

\# -----------------------------



def generate\_study\_plan(stress\_level, student\_data):

&nbsp;   plan = {}



&nbsp;   if stress\_level == "High":

&nbsp;       plan\['Priority'] = "Critical"

&nbsp;       plan\['Recommendations'] = \[

&nbsp;           "Break tasks into small daily goals",

&nbsp;           "Focus on nearest deadlines first",

&nbsp;           "Increase study time gradually",

&nbsp;           "Ensure at least 7 hours of sleep"

&nbsp;       ]



&nbsp;   elif stress\_level == "Medium":

&nbsp;       plan\['Priority'] = "Moderate"

&nbsp;       plan\['Recommendations'] = \[

&nbsp;           "Use Pomodoro technique",

&nbsp;           "Allocate more time to difficult subjects",

&nbsp;           "Maintain consistent study schedule"

&nbsp;       ]



&nbsp;   else:

&nbsp;       plan\['Priority'] = "Low"

&nbsp;       plan\['Recommendations'] = \[

&nbsp;           "Maintain current routine",

&nbsp;           "Revise topics weekly",

&nbsp;           "Avoid overloading yourself"

&nbsp;       ]



&nbsp;   return plan



\# -----------------------------

\# 4. FULL PIPELINE FUNCTION

\# -----------------------------



def stress\_prediction\_pipeline(student\_input):

&nbsp;   input\_df = pd.DataFrame(\[student\_input])

&nbsp;   stress\_level = model.predict(input\_df)\[0]

&nbsp;   study\_plan = generate\_study\_plan(stress\_level, student\_input)

&nbsp;   return stress\_level, study\_plan



\# -----------------------------

\# 5. TEST THE COMPLETE SYSTEM

\# -----------------------------

student\_input = {

&nbsp;   "Subjects": 5,

&nbsp;   "Tasks": 9,

&nbsp;   "Difficulty": 4,

&nbsp;   "Deadlines": 3,

&nbsp;   "StudyHours": 2,

&nbsp;   "Sleep": 5,

&nbsp;   "ExamDays": 7

}



predicted\_stress, plan = stress\_prediction\_pipeline(student\_input)



print("Predicted Stress Level:", predicted\_stress)

print("\\nPersonalized Study Plan:")

for tip in plan\['Recommendations']:

&nbsp;   print("-", tip)



