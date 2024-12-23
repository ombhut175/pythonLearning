class Employee:
    name = str()

    @property
    def name(self):
        return f"name method"
    @name.setter
    def name(self,name):
        self.fName = name.split()[0]
        self.lName = name.split()[1]


emp = Employee()

emp.name = "yash patoliya"

print(f"{emp.name}")