# Employee Class unit tests
# This file contains all tests for the Employee class.

import unittest
from employee import Employee, EmployeeType


class NameTests(unittest.TestCase):
    """ Tests related to employee name. """

    def test_hasName(self):
        testName = "Jane"
        person = Employee(testName, EmployeeType.FULLTIME)
        self.assertEqual(testName, person.name, msg="Name doesn't match.")


class YearsTests(unittest.TestCase):
    """ Tests related to employee years. """

    def test_hasYears(self):
        years = 4
        person = Employee("Jane", EmployeeType.FULLTIME, years)
        self.assertEqual(years, person.years, msg="Years of service doesn't match.")

    def test_negativeYears(self):
        self.assertRaises(ValueError, Employee, "Jane", EmployeeType.FULLTIME, -4)


class ETypeTests(unittest.TestCase):
    """ Tests related to employee type. """

    def test_fulltime(self):
        person = Employee("Jane", EmployeeType.FULLTIME)
        self.assertEqual(EmployeeType.FULLTIME, person.etype)

    def test_contractor(self):
        person = Employee("Jane", EmployeeType.CONTRACTOR)
        self.assertEqual(EmployeeType.CONTRACTOR, person.etype)

    def test_temp(self):
        person = Employee("Jane", EmployeeType.TEMPORARY)
        self.assertEqual(EmployeeType.TEMPORARY, person.etype)

    def test_invalidType(self):
        with self.assertRaises(TypeError, msg="Accepted invalid employee type"):
            Employee("Jane", 2)
        with self.assertRaises(TypeError, msg="Accepted invalid employee type"):
            Employee("Jane", "foo")


class VactionTests(unittest.TestCase):
    """ Tests related to number of vacation days. """

    VDAYS_PER_YEAR = 5

    def test_newFulltime(self):
        years = 0
        expected = self.VDAYS_PER_YEAR * years
        person = Employee("Jane", EmployeeType.FULLTIME, years)
        self.assertEqual(expected, person.getVacation())

    def test_seasonedFulltime(self):
        years = 11
        expected = self.VDAYS_PER_YEAR * years
        person = Employee("Jane", EmployeeType.FULLTIME, years)
        self.assertEqual(expected, person.getVacation())

    def test_fractionalVacation(self):
        years = 0.711
        expected = self.VDAYS_PER_YEAR * years
        person = Employee("Joe", EmployeeType.FULLTIME, years)
        self.assertEqual(expected, person.getVacation())

    def test_contractor(self):
        person = Employee("Joe", EmployeeType.CONTRACTOR, 20)
        self.assertEqual(0, person.getVacation())

    def test_temp(self):
        person = Employee("Joe", EmployeeType.TEMPORARY, 20)
        self.assertEqual(0, person.getVacation())


# Run all tests
if __name__ == '__main__':
    unittest.main()

