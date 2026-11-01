import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


data = pd.read_csv("student-mat.csv", sep=";")


features = [
    "studytime",
    "failures",
    "freetime",
    "goout",
    "health",
    "absences",
    "G1",
    "G2"
]

X = data[features]
y = data["G3"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully!")
print("Mean Absolute Error:", mae)


joblib.dump(model, "model/student_model.pkl")

print("Model saved successfully!")