import json
from config import DATA_FILE
from services.tax_service import apply_tax
from services.data_service import load_employees
from utils.rules import role_bonus, overtime_adjustment, department_label

def calculate_final_salary(employee):
    total = employee["salary"]
    total = total + role_bonus(employee["role"], employee["bonus"])
    total = total + overtime_adjustment(employee["hours"])
    total = apply_tax(total)
    return total

def payroll_snapshot():
    data = load_employees()
    result = []
    for employee in data:
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
    data = load_employees()
    result = {}
    for employee in data:
        department = employee["department"]
        if department not in result:
            result[department] = 0
        result[department] = result[department] + calculate_final_salary(employee)
    return result
