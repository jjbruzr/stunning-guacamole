# This is the class demo creating a payroll system.

# create the Employy class and initialize it's properties
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

# create a method to calculate weekly paychecm amount
    def calculate_paycheck(self):
        return self.salary/52
    
