from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/student_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        studytime = float(request.form["studytime"])
        failures = float(request.form["failures"])
        freetime = float(request.form["freetime"])
        goout = float(request.form["goout"])
        health = float(request.form["health"])
        absences = float(request.form["absences"])
        G1 = float(request.form["G1"])
        G2 = float(request.form["G2"])

        input_data = np.array([[
            studytime,
            failures,
            freetime,
            goout,
            health,
            absences,
            G1,
            G2
        ]])

        prediction = model.predict(input_data)[0]

        if prediction >= 16:
            performance = "Excellent"
        elif prediction >= 12:
            performance = "Good"
        elif prediction >= 10:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        result = f"Predicted Final Grade (G3): {prediction:.2f} / 20"

        return render_template(
            "predict.html",
            result=result,
            performance=performance
        )

    return render_template("predict.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True)