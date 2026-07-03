"""
Tests for the department total cost report evolution (TP2).

These tests are written in pytest style (assert-based, function-per-scenario)
and can be run with `pytest tests/` once pytest is available.

They build PayrollService instances directly with in-memory employee data
(bypassing load_employees/JSON file access) so the report logic can be
tested in isolation, including edge cases that do not exist in the current
employees.json (missing/invalid department).
"""

from services.payroll_service import PayrollService


def make_service(employees):
    """Builds a PayrollService without touching the JSON file/data_service."""
    service = PayrollService.__new__(PayrollService)
    service.employees = employees
    return service


def test_department_grouping_basic():
    employees = [
        {"name": "Ana", "role": "dev", "salary": 5000, "hours": 170, "bonus": True, "department": "engineering"},
        {"name": "Bruna", "role": "support", "salary": 3200, "hours": 160, "bonus": False, "department": "operations"},
    ]
    service = make_service(employees)
    report = service.get_department_cost_report()
    departments = [d["department"] for d in report]
    assert "Engineering" in departments
    assert "Operations" in departments


def test_total_cost_matches_sum_of_individual_costs():
    employees = [
        {"name": "Ana", "role": "dev", "salary": 5000, "hours": 170, "bonus": True, "department": "engineering"},
        {"name": "Diego", "role": "dev", "salary": 6200, "hours": 190, "bonus": True, "department": "engineering"},
    ]
    service = make_service(employees)
    report = service.get_department_cost_report()
    engineering = next(d for d in report if d["department"] == "Engineering")

    expected_total = sum(service.calculate_final_salary(e) for e in employees)
    assert engineering["employee_count"] == 2
    assert round(engineering["total_cost"], 2) == round(expected_total, 2)
    assert round(engineering["average_cost"], 2) == round(expected_total / 2, 2)


def test_missing_department_is_grouped_as_not_informed():
    employees = [
        {"name": "X", "role": "dev", "salary": 4000, "hours": 170, "bonus": False, "department": ""},
    ]
    service = make_service(employees)
    report = service.get_department_cost_report()
    assert len(report) == 1
    assert report[0]["department"] == "Not informed"


def test_unknown_department_is_grouped_as_other():
    employees = [
        {"name": "Y", "role": "manager", "salary": 6000, "hours": 170, "bonus": False, "department": "marketing"},
    ]
    service = make_service(employees)
    report = service.get_department_cost_report()
    assert report[0]["department"] == "Other"


def test_missing_department_key_does_not_raise():
    # Defensive: department key not present at all in the dict.
    employees = [
        {"name": "Z", "role": "support", "salary": 3000, "hours": 160, "bonus": False},
    ]
    service = make_service(employees)
    report = service.get_department_cost_report()
    assert report[0]["department"] == "Not informed"


def test_empty_employee_list_returns_empty_report():
    service = make_service([])
    assert service.get_department_cost_report() == []


def test_report_is_sorted_by_department_name():
    employees = [
        {"name": "Carlos", "role": "manager", "salary": 9000, "hours": 185, "bonus": True, "department": "management"},
        {"name": "Ana", "role": "dev", "salary": 5000, "hours": 170, "bonus": True, "department": "engineering"},
    ]
    service = make_service(employees)
    report = service.get_department_cost_report()
    labels = [d["department"] for d in report]
    assert labels == sorted(labels)


def test_existing_department_summary_still_works_unchanged():
    """Regression check: pre-existing method must keep working as before."""
    employees = [
        {"name": "Ana", "role": "dev", "salary": 5000, "hours": 170, "bonus": True, "department": "engineering"},
    ]
    service = make_service(employees)
    summary = service.department_summary()
    assert "engineering" in summary
    assert round(summary["engineering"], 2) == round(service.calculate_final_salary(employees[0]), 2)


def test_existing_payroll_snapshot_still_works_unchanged():
    """Regression check: core salary calculation must be untouched."""
    employees = [
        {"name": "Ana", "role": "dev", "salary": 5000, "hours": 170, "bonus": True, "department": "engineering"},
    ]
    service = make_service(employees)
    snapshot = service.payroll_snapshot()
    assert snapshot[0]["name"] == "Ana"
    assert snapshot[0]["final_salary"] == service.calculate_final_salary(employees[0])
