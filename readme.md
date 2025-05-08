# Student Score Predictor 📈

This project uses a simple **Linear Regression** model to predict a student's exam score based on how many hours they studied.

---

## 🔧 How It Works

---

## 📚 Understanding Linear Regression (Beginner-Friendly)

**Linear Regression** is one of the simplest and most widely used Machine Learning algorithms. It’s used to find the **relationship between two variables** by fitting a straight line (called a *regression line*) through a set of data points.

---

### 🔢 What It Does

In basic terms, linear regression answers the question:

> ❓ "Can I predict one value (like a test score) based on another value (like hours studied)?"

It works by finding a **line of best fit** between the input (X) and output (Y), using the formula:


Y = mX + b

Where:

Y = predicted value (exam score)

X = input value (hours studied)

m = slope of the line (how much Y changes per unit of X)

b = intercept (where the line crosses the Y-axis)

In this project, I trained a linear regression model to learn the relationship between:

Feature (X)	Target (Y)
Hours Studied	Exam Score

Here’s the actual training data used:

Hours	Score
1	35
2	45
3	50
4	60
5	65
6	70
7	75
8	85
9	95

The algorithm analyzed this data and found the best-fitting line that maps hours studied to expected exam score.

Once trained, the model can be used to make predictions like:

Hours Studied	Predicted Score
2	~44.56
4.5	~62.88
6.5	~73.45
10	~100.12 (extrapolated)*

Note: Predictions for inputs outside the original data range (like 10 hours) are called extrapolations. They can be less accurate.

- Input: Number of hours studied
- Output: Predicted exam score
- Model: Trained using scikit-learn's `LinearRegression`

---

## 🧠 Example

```bash
Predicted Score for 6.5 hours of study: 72.25
