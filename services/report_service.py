from services.payroll_service import PayrollService

payroll_service = PayrollService()

def print_payroll():
    print("=== PAYROLL REPORT ===")
    total_company = payroll_service.get_total_company_cost()
    by_role = payroll_service.get_role_counts()
    for employee in payroll_service.payroll_snapshot():
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
    for department, total in payroll_service.department_summary().items():
        print(department, total)