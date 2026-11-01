# MindSync AI – Student Performance Prediction System

MindSync AI is a Machine Learning based web application that predicts students' final academic grades using academic and lifestyle-related information.

The system uses a trained Random Forest Regression model to estimate the final student grade (G3) based on previous academic performance and other student-related factors.

## Features

- Student final grade prediction
- Machine Learning based analysis
- Performance level classification
- Interactive web interface
- Student information analysis
- Personal project and developer information

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS

## Machine Learning Model

**Algorithm:** Random Forest Regressor

**Prediction Target:** Final Grade (G3)

**Input Features:**
1. Study Time
2. Previous Failures
3. Free Time
4. Going Out
5. Health
6. Absences
7. First Period Grade (G1)
8. Second Period Grade (G2)

**Model Evaluation:**

Mean Absolute Error (MAE): 1.1361

## Project Structure

```text
MindSyncAI/
│
├── app.py
├── train_model.py
├── student-mat.csv
│
├── model/
│   └── student_model.pkl
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── predict.html
│   ├── dashboard.html
│   └── contact.html
│
├── static/
│   ├── style.css
│   ├── image/
│   └── js/
│
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yashsonu7200/MindSyncAI.git
```

### 2. Open Project Folder

```bash
cd MindSyncAI
```

### 3. Install Required Libraries

```bash
pip install flask pandas numpy scikit-learn joblib
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

## Developer

**Yash Kumar Srivastava**

B.Tech – Computer Science and Engineering (Artificial Intelligence)

- LinkedIn: https://www.linkedin.com/in/yash-kumar-srivastava-841002339
- Instagram: https://www.instagram.com/__yash.sonu/

## Project Objective

The objective of MindSync AI is to demonstrate how Machine Learning can be used to estimate student academic performance through a simple and interactive web application.

---

© 2026 MindSync AI
