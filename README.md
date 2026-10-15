# 🎓 Academic Stress Prediction Model

A machine learning project that predicts a student's **academic stress level** (Low / Medium / High) from their workload and study habits, then generates a **personalised study plan** to help reduce that stress.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-Data-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-013243?logo=numpy&logoColor=white)

---

## 📌 Overview

Students often struggle with heavy workloads, tight deadlines and too little sleep, but stress is rarely detected early. This project:

1. Builds a dataset of academic factors for 300 students
2. Labels each student's stress level with an interpretable scoring rule
3. Trains a **Decision Tree classifier** to predict stress
4. Recommends a study plan matched to the predicted stress level

## 🧠 Features used

| Feature | Description |
|---|---|
| `Subjects` | Number of enrolled subjects |
| `Tasks` | Pending assignments / tasks |
| `Difficulty` | Course difficulty (1–5) |
| `Deadlines` | Days until the nearest deadline |
| `StudyHours` | Daily study hours |
| `Sleep` | Daily sleep hours |
| `ExamDays` | Days until the next exam |

## ⚙️ How it works

```
Student input ─► Decision Tree (max_depth=5) ─► Stress level ─► Study plan
```

| Predicted stress | Priority | Example recommendations |
|---|---|---|
| 🔴 High | Critical | Break tasks into small daily goals, focus on nearest deadlines, sleep ≥ 7 h |
| 🟡 Medium | Moderate | Pomodoro technique, more time for difficult subjects |
| 🟢 Low | Low | Keep current routine, weekly revision |

## 🚀 Run it

```bash
git clone https://github.com/Nadvi-Ekram/Academic-stress-Prediction-Model.git
cd Academic-stress-Prediction-Model
pip install -r requirements.txt
python stress_model.py
```

**Sample output**

```
Model accuracy on test set: 88.33%
Predicted Stress Level: Medium

Personalized Study Plan:
- Use Pomodoro technique
- Allocate more time to difficult subjects
- Maintain consistent study schedule
```

To test your own case, edit the `student_input` dictionary at the bottom of `stress_model.py`.

## 📁 Files

| File | Contents |
|---|---|
| `stress_model.py` | Full runnable pipeline (dataset → training → prediction → study plan) |
| `requirements.txt` | Python dependencies |
| `Project Report (ASPM).pdf` | Full project report |
| `Python code (ASPM).md` | Original code notes |

## 🔮 Future work

- Train on a real student survey dataset instead of synthetic data
- Compare with Random Forest and Logistic Regression
- Add a **Streamlit** web interface for live predictions

---

📍 Course project, Department of CSE, **Southeast University**
