import json
from config import DATA_FILE
from services.tax_service import apply_tax_again
from utils.rules import role_bonus_again, overtime_adjustment, department_label

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def calculate_final_salary(employee):
    total = employee["salary"]
    total = total + role_bonus_again(employee["role"], employee["bonus"])
    total = total + overtime_adjustment(employee["hours"])
    total = apply_tax_again(total)
    return total

def payroll_snapshot():
    data = load_data()
    result = []
    for employee in data["employees"]:
        final_salary = calculate_final_salary(employee)
        classification = "standard"
        if final_salary > 7000:
            classification = "high_cost"
        elif final_salary < 3000:
            classification = "low_cost"

        result.append({
            "name": employee["name"],
            "role": employee["role"],
            "department": department_label(employee["department"]),
            "base_salary": employee["salary"],
            "final_salary": final_salary,
            "classification": classification
        })
    return result

def department_summary():
    data = load_data()
    result = {}
    for employee in data["employees"]:
        department = employee["department"]
        if department not in result:
            result[department] = 0
        result[department] = result[department] + calculate_final_salary(employee)
    return result
