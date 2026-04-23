from services.payroll_service import payroll_snapshot, department_summary

def print_payroll():
    print("=== PAYROLL REPORT ===")
    total_company = 0
    by_role = {}
    for employee in payroll_snapshot():
        total_company = total_company + employee["final_salary"]

        if employee["role"] not in by_role:
            by_role[employee["role"]] = 0
        by_role[employee["role"]] = by_role[employee["role"]] + 1

        print("Name:", employee["name"])
        print("Role:", employee["role"])
        print("Department:", employee["department"])
        print("Base salary:", employee["base_salary"])
        print("Final salary:", employee["final_salary"])
        print("Classification:", employee["classification"])
        print("----------------")

    print("TOTAL COMPANY COST:", total_company)
    print("BY ROLE:", by_role)

def print_department_costs():
    print("=== DEPARTMENT COSTS ===")
    for department, total in department_summary().items():
        print(department, total)
