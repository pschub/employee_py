# Employee Module
# This file contains the Employee class and the EmployeeType enum.

from enum import Enum

class EmployeeType(Enum):
    """ Describes employee types (Fulltime, contractor, temp). """
    FULLTIME = 0,
    CONTRACTOR = 1,
    TEMPORARY = 2,

class Employee:
    """ Describes an employee. Employees may be any of the types given by the
        EmployeeType enum. Fulltime employees receive vacation at a rate given
        by VACATION_DAYS_PER_YEAR.
    """

    VACATION_DAYS_PER_YEAR = 5

    def __init__(self, name, etype, years=0):
        """ Create an employee.
              name  - Name of employee.
              etype - Type of employee. Will raise TypeError if not a valid
                      EmployeeType.
              years - Optional arg to specify years of service. Will raise
                      ValueError if negative.
            """

        self.name = name
        if not isinstance(etype, EmployeeType):
            raise TypeError("Invalid employee type: {}".format(type(etype)))
        self.etype = etype

        if (years < 0):
            raise ValueError("Invalid employee years: {}".format(years))

        self.years = years
        return

    def getVacation(self):
        """ Return the number of vacation days the employee has accrued."""
        if (self.etype != EmployeeType.FULLTIME):
            return 0
        return self.years * self.VACATION_DAYS_PER_YEAR
