class Employee:
    def __init__(self, name, role, salary, hours, bonus, department):
        self.name = name
        self.role = role
        self.salary = salary
        self.hours = hours
        self.bonus = bonus
        self.department = department

    def describe(self):
        return f"{self.name} - {self.role} ({self.department})"
