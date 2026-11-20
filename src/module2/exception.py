
class InvalidSalaryError(Exception):
    pass
 
 
def calculate(salary):
    if salary <= 0:
        raise InvalidSalaryError("Salary must be greater than zero")
 
    print("Valid salary:", salary)
 
 
try:
    calculate(0)
 
except InvalidSalaryError as e:
    print("Error:", e)