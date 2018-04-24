# Employee Demo
# This file demonstrates the Employee class by creating a list of employees and
# printing their data to stdout.

from employee import Employee, EmployeeType


def printEmployee(employee):
    """ Pretty-print an employee to stdout. """
    typeString = ""
    if (employee.etype == EmployeeType.FULLTIME):
        typeString = "FT"
    elif (employee.etype == EmployeeType.CONTRACTOR):
        typeString = "C"
    elif (employee.etype == EmployeeType.TEMPORARY):
        typeString = "T"
    else:
        typeString = "?"

    name = employee.name
    years = employee.years
    vacation = employee.getVacation()
    if (vacation == 0):
        vacation = "None"
    template = "Name: {} [{}], Duration: {} years, Vacation Accrued: {} days"

    print(template.format(name, typeString, years, vacation))
    return


if __name__=="__main__":
    # List of employees
    people = (Employee("Alice",   EmployeeType.FULLTIME,   1.5),
              Employee("Bob",     EmployeeType.FULLTIME,   2),
              Employee("Charlie", EmployeeType.CONTRACTOR, 1.3),
              Employee("David",   EmployeeType.TEMPORARY,  0.1),
              Employee("Erin",    EmployeeType.TEMPORARY,  2),
              Employee("Francis", EmployeeType.CONTRACTOR, 3),
              )

    # Print all employees
    for person in people:
        printEmployee(person)
