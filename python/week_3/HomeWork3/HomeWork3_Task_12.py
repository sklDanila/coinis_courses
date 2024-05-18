# task_12

class Company:
    def __init__(self, name: str, area: str, balance: float, max_num_of_employees: int):
        self.name = name
        self.area = area
        self.employees = []
        self.balance = balance
        self.max_num_of_employees = max_num_of_employees
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    def get_area(self):
        return self.area
    
    def set_area(self, area):
        self.area = area
        
    def get_balance(self):
        return self.balance
    
    def set_balance(self, balance):
        if balance > 0:
            self.balance = balance
    
    def get_max_num_of_employees(self):
        return self.max_num_of_employees
    
    def set_max_num_of_employees(self, max_num_of_employees):
        if max_num_of_employees > 0:
            self.max_num_of_employees = max_num_of_employees
            
            
    def add_employee(self, employee):
        if len(self.employees) < self.get_max_num_of_employees():
            self.employees.append(dict(employee))
            print("Employee added successfully.")
        else:
            print("The company has reached its maximum number of employees.")
    
    def remove_employee(self, employee_name, employee_surname):
        for employee in self.employees:
            if employee["name"] == employee_name and employee["surname"] == employee_surname:
                self.employees.remove(employee)
                print("Employee removed successfully.")
                break
        else:
            print("Employee not found.")
            
    def str(self):
        return f'"name: "{self.get_name},\n"area: "{self.get_area},\n"balance: "{self.get_balance}\n'
    
    def can_pay_employees(self):
        money = self.get_balance()
        for employee in self.employees:
            money -= float(employee["salary"])
        if money < 0:
            return False
        else:
            return True
        
    def gt(self, other_company):
        return len(self.employees) > len(other_company.employees)
    

company1 = Company("Company A", "IT", 10000.0, 50)
company2 = Company("Company B", "Finance", 5000.0, 30)


if company1.gt(company2):
    print(f"{company1.name} has more employees than {company2.name}.")
else:
    print(f"{company2.name} has more employees than {company1.name}.")
    
company1.add_employee({'name': 'John', 'surname': 'Doe', 'salary': 5000})
company1.add_employee({'name': 'Jane', 'surname': 'Smith', 'salary': 6000})
company1.add_employee({'name': 'Alex', 'surname': 'Johnson', 'salary': 5500})

company1.remove_employee('John', 'Doe')

print(str(company1))

print("Company can pay employees:", company1.can_pay_employees())

print("Company 1 is greater than company 2:", company1.gt(company2))