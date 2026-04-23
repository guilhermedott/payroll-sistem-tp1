import json
from config import DATA_FILE

def validate_employee(employee):
    if not isinstance(employee.get("name"), str) or not employee["name"].strip():
        raise ValueError(f"Invalid name for employee: {employee}")
    if not isinstance(employee.get("role"), str) or employee["role"] not in ["dev", "manager", "support"]:
        raise ValueError(f"Invalid role for employee {employee['name']}: {employee['role']}")
    if not isinstance(employee.get("salary"), (int, float)) or employee["salary"] <= 0:
        raise ValueError(f"Invalid salary for employee {employee['name']}: {employee['salary']}")
    if not isinstance(employee.get("hours"), int) or not (0 <= employee["hours"] <= 300):
        raise ValueError(f"Invalid hours for employee {employee['name']}: {employee['hours']}")
    if not isinstance(employee.get("bonus"), bool):
        raise ValueError(f"Invalid bonus for employee {employee['name']}: {employee['bonus']}")
    if not isinstance(employee.get("department"), str) or not employee["department"].strip():
        raise ValueError(f"Invalid department for employee {employee['name']}: {employee['department']}")

def load_employees():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    employees = data["employees"]
    for emp in employees:
        validate_employee(emp)
    return employees