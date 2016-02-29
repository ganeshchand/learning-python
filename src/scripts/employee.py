#!/usr/bin/python


class Employee:
    # Class documentation:
    """Common base class for all employees """
    empCount = 0  # static variable or class attribute

    def __init__(self, name, salary):  # these are instance variables
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod # static method or class method
    def displayEmployeeCount():
        print("Total Employee: {}".format(Employee.empCount))

    def getName(self):  # instance method
        return self.name

    def getSalary(self):  # instance method
        return self.salary

    def __str__(self):  # toString
        return "Employee: [name: {}, salary: {}]".format(self.name, self.salary)

    def displayEmployeeInfo(self):
        return "Name: {}, Salary: {}".format(self.name, self.salary)

if __name__ == "__main__":
    emp1 = Employee("Zara", 2000)
    print("Created employee: {}".format(emp1))
    print(str(emp1))
    Employee.displayEmployeeCount()
    emp2 = Employee("Manni", 3000)
    print("Created employee: {}".format(emp2))
    Employee.displayEmployeeCount()

    print("About this class: {}".format(Employee.__doc__))
    print("Class Name: {}".format(Employee.__name__))
    print("Module Name: {}".format(Employee.__module__))
    print("You can also try other built-in class attributes : __dict__ and __bases__")
