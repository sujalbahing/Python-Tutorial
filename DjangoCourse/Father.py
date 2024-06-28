# class Father:
#     def __init__(self, name):
#         self.name = name
        
#     def talk(self):
#         print(self.name)
#         print('I can talk')
        
# class Ram(Father):
    
#     def walk(self):
#         print('I can walk')
        
# ram = Ram('Ram')
# ram.talk()

# class Shyam(Father):
#     def walk(self):
#         print('I can walk')
        
# shyam = Shyam('Shyam')
# shyam.talk()
    
    

class Employee:
    def __init__(self, name, emp_id):
        self._name = name
        self._emp_id = emp_id
    
    def display_info(self):
        print(f'Name: {self._name}')
        print(f'Employee ID: {self._emp_id}')
        
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name,emp_id)
        self.department = department
        
    def display_info(self):
        super().display_info()
        print(f'Department: {self.department}')
        
class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language
        
    def display_info(self):
        super().display_info()
        print(f'Programming Language: {self.programming_language}')
        
manager = Manager('Bob',1,'Engineering')
manager.display_info()

developer = Developer('Alice',2,'Python')
developer.display_info()