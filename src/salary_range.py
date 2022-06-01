def validate_salary(salary):
    if type(salary) != int:
        raise(ValueError)
