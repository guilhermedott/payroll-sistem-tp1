def role_bonus(role, bonus_enabled):
    if role == "dev":
        return 500 if bonus_enabled else 0
    elif role == "manager":
        return 1500 if bonus_enabled else 0
    elif role == "support":
        return 200 if bonus_enabled else 0
    return 0

def role_bonus_again(role, bonus_enabled):
    if role == "dev":
        return 500 if bonus_enabled else 0
    elif role == "manager":
        return 1500 if bonus_enabled else 0
    elif role == "support":
        return 200 if bonus_enabled else 0
    return 0

def overtime_adjustment(hours):
    if hours > 180:
        return 300
    elif hours < 160:
        return -100
    return 0

def department_label(department):
    if department == "engineering":
        return "Engineering"
    elif department == "management":
        return "Management"
    elif department == "operations":
        return "Operations"
    return "Other"
