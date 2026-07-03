def role_bonus(role, bonus_enabled):
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

DEPARTMENT_LABELS = {
    "engineering": "Engineering",
    "management": "Management",
    "operations": "Operations",
}

def department_label(department):
    # Missing/empty/non-string department -> explicit "Not informed" label.
    # This keeps reports from crashing or silently mixing these employees
    # with the generic "Other" bucket used for unknown-but-present values.
    if not isinstance(department, str) or not department.strip():
        return "Not informed"

    return DEPARTMENT_LABELS.get(department, "Other")
