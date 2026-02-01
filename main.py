from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load the CSV
df = pd.read_csv("pay_matrix.csv")

@app.get("/")
def home():
    return {"message": "Pay Matrix FastAPI is running!"}

@app.get("/check_salary/")
def check_salary(level: int, cell: int, salary: int):
    try:
        row = df[(df["Level"] == level) & (df["Cell"] == cell)].iloc[0]
    except:
        return {"error": "Level or Cell not found in CSV"}

    min_pay = row["Minimum"]
    max_pay = row["Maximum"]

    if salary < min_pay:
        status = "Below Range"
    elif salary > max_pay:
        status = "Above Range"
    else:
        status = "Within Range"

    return {
        "Level": level,
        "Cell": cell,
        "Entered Salary": salary,
        "Minimum Allowed": min_pay,
        "Maximum Allowed": max_pay,
        "Status": status
    }
