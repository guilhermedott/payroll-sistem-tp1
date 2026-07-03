from services.report_service import print_payroll, print_department_costs, print_department_cost_report
from services.payroll_service import PayrollService

def main():
    while True:
        print("1 - Print payroll")
        print("2 - Print department costs")
        print("3 - Snapshot")
        print("4 - Print department total cost report")
        print("5 - Exit")

        op = input("Choose: ")

        if op == "1":
            print_payroll()
        elif op == "2":
            print_department_costs()
        elif op == "3":
            service = PayrollService()
            print("SNAPSHOT:", service.payroll_snapshot())
        elif op == "4":
            print_department_cost_report()
        elif op == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
