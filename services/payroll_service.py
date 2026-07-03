from services.data_service import load_employees
from services.tax_service import apply_tax
from utils.rules import role_bonus, overtime_adjustment, department_label

class PayrollService:
    def __init__(self):
        self.employees = load_employees()

    def calculate_final_salary(self, employee):
        total = employee["salary"]
        total = total + role_bonus(employee["role"], employee["bonus"])
        total = total + overtime_adjustment(employee["hours"])
        total = apply_tax(total)
        return total

    def payroll_snapshot(self):
        result = []
        for employee in self.employees:
            final_salary = self.calculate_final_salary(employee)
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

    def department_summary(self):
        result = {}
        for employee in self.employees:
            department = employee["department"]
            if department not in result:
                result[department] = 0
            result[department] = result[department] + self.calculate_final_salary(employee)
        return result

    def get_department_cost_report(self):
        """
        Builds a detailed cost report grouped by department.

        For each department returns the list of employees with their
        individual final salary (cost to the company), the employee count,
        the total cost and the average cost per employee.

        Employees with a missing or unrecognized department are grouped
        under a normalized label ("Not informed" or "Other") instead of
        raising an error or being silently dropped, so the report never
        breaks due to inconsistent department data.
        """
        groups = {}
        for employee in self.employees:
            department_key = department_label(employee.get("department"))
            final_salary = self.calculate_final_salary(employee)

            if department_key not in groups:
                groups[department_key] = {"employees": [], "total_cost": 0.0}

            groups[department_key]["employees"].append({
                "name": employee["name"],
                "role": employee["role"],
                "final_salary": round(final_salary, 2),
            })
            groups[department_key]["total_cost"] += final_salary

        report = []
        for department, info in sorted(groups.items()):
            employee_count = len(info["employees"])
            total_cost = info["total_cost"]
            average_cost = total_cost / employee_count if employee_count else 0

            report.append({
                "department": department,
                "employees": sorted(info["employees"], key=lambda e: e["name"]),
                "employee_count": employee_count,
                "total_cost": round(total_cost, 2),
                "average_cost": round(average_cost, 2),
            })

        return report

    def get_total_company_cost(self):
        snapshot = self.payroll_snapshot()
        return sum(employee["final_salary"] for employee in snapshot)

    def get_role_counts(self):
        snapshot = self.payroll_snapshot()
        result = {}
        for employee in snapshot:
            role = employee["role"]
            if role not in result:
                result[role] = 0
            result[role] = result[role] + 1
        return result