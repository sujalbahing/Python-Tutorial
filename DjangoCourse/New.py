class Employee:
    
    def __init__(self, name, emp_id, salary):

        self._name = name
        self._emp_id = emp_id
        self._salary = salary
        
    def calculate_bonus(self):
        return self._salary * 0.1
    
    def display_info(self):
        print(f"Name: ${self._name}")
        print(f"Employee id : ${self._emp_id}")
        print(f"Salary : ${self._salary}")
        
employee = Employee('Bob',1,1000)
employee.display_info()
bonus = employee.calculate_bonus()

print(bonus)



    