from services.report_service import print_payroll, print_department_costs
from services.payroll_service import payroll_snapshot

def main():
    while True:
        print("1 - Print payroll")
        print("2 - Print department costs")
        print("3 - Snapshot")
        print("4 - Exit")

        op = input("Choose: ")

        if op == "1":
            print_payroll()
        elif op == "2":
            print_department_costs()
        elif op == "3":
            print("SNAPSHOT:", payroll_snapshot())
        elif op == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
