# 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.
class Employee:
    salary = int()
    increament = int()

    def setSalary(self,salary):
        self.salary = salary
    def increaseSalary(self,increamentVal):
        self.salary += increamentVal
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increament)
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,newSal):
        self.increament = (newSal-self.salary)/self.salary


employee = Employee()
employee.salary = 12000


employee.salaryAfterIncrement = 14000

print(employee.salaryAfterIncrement)