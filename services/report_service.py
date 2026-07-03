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

def print_department_cost_report():
    print("=== DEPARTMENT TOTAL COST REPORT ===")
    report = payroll_service.get_department_cost_report()

    if not report:
        print("No employees found.")
        return

    grand_total = 0
    for department in report:
        print(f"\nDepartment: {department['department']}")
        print(f"{'Name':<15}{'Role':<12}{'Final Salary':>15}")
        print("-" * 42)
        for employee in department["employees"]:
            print(f"{employee['name']:<15}{employee['role']:<12}{employee['final_salary']:>15.2f}")
        print("-" * 42)
        print(f"Employees: {department['employee_count']}   "
              f"Total: {department['total_cost']:.2f}   "
              f"Average: {department['average_cost']:.2f}")
        grand_total += department["total_cost"]

    print("\n" + "=" * 42)
    print(f"GRAND TOTAL (ALL DEPARTMENTS): {grand_total:.2f}")