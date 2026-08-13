class Employee:
    def __init__(self, name, basicsalary):
        self.name=name
        self.basicsalary=basicsalary 
        
    def calculatesalary(self):
        print(self.basicsalary)
        
class Developer(Employee):
    def __init__(self, name, basicsalary, codingbonus):
        super().__init__(name, basicsalary)
        self.codingbonus=codingbonus 
        
    def calculatesalary(self):
        print(self.basicsalary+self.codingbonus)
        
class Designer(Employee):
    def __init__(self, name, basicsalary, designbonus):
        super().__init__(name, basicsalary)
        self.designbonus=designbonus 
        
    def calculatesalary(self):
        print(self.basicsalary+self.designbonus)
        
class Manager(Employee):
    def __init__(self, name, basicsalary, managementbonus):
        super().__init__(name, basicsalary)
        self.managementbonus=managementbonus
        
    def calculatesalary(self):
        print(self.basicsalary+self.managementbonus)
        
d1=Designer("Shruti",100000,800)
d1.calculatesalary()
