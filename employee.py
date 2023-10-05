"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.output = salaryCalculator(self.name)
    def get_pay(self):
        return self.output.salaryCalculate()

    def __str__(self):
        self.name = self.output.outputPrint()
        print(self.name)
        return str(self.name)

class salaryCalculator(Employee):
    def __init__(self, name, salary = 0, hourContract = 0, bonusCom = 0, contractCom = 0, contractNum = 0, numOfHours = 0):
        self.salary = salary
        self.hourContract = hourContract
        self.bonusCom = bonusCom
        self.contractCom = contractCom
        self.contractNum = contractNum
        self.numOfHours = numOfHours
        self.name = name
        if (self.name == "Billie"):
            self.salary = 4000
        elif (self.name == "Charlie"):
            self.hourContract = 25
            self.numOfHours = 100
        elif (self.name == "Renee"):
            self.salary = 3000 
            self.contractCom = 200 
            self.contractNum = 4
        elif (self.name == "Jan"):
            self.hourContract = 25
            self.numOfHours = 150
            self.contractCom = 220
            self.contractNum = 3
        elif (self.name == "Robbie"):
            self.salary = 2000 
            self.bonusCom = 1500
        elif (self.name == "Ariel"):
            self.hourContract = 30
            self.numOfHours = 120
            self.bonusCom = 600
        
    def outputPrint(self):
        text = ''
        if (self.salary != 0):
            if (self.bonusCom != 0):
                text += (f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonusCom}.')
            elif (self.contractCom != 0 and self.contractNum != 0):
                text += (f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contractNum} contract(s) at {self.contractCom}/contract.")
            else:
                text += (f"{self.name} works on a monthly salary of {self.salary}.")
        if (self.hourContract != 0 and self.numOfHours != 0):
            if (self.bonusCom != 0):
                text += (f'{self.name} works on a contract of {self.numOfHours} hours at {self.hourContract}/hour and receives a bonus commission of {self.bonusCom}.')
            elif (self.contractCom != 0 and self.contractNum != 0):
                text += (f"{self.name} works on a contract of {self.numOfHours} hours at {self.hourContract}/hour and receives a commission for {self.contractNum} contract(s) at {self.contractCom}/contract.")
            else:
                text += (f"{self.name} works on a contract of {self.numOfHours} hours at {self.hourContract}/hour.")
        text += (f' Their total pay is {self.salaryCalculate()}.')
        return text

    def salaryCalculate(self):
        if (self.salary != 0):
            if (self.bonusCom != 0):
                return self.salary + self.bonusCom
            elif (self.contractCom != 0 and self.contractNum != 0):
                return self.salary + self.contractCom * self.contractNum
            else:
                return self.salary
        if (self.hourContract != 0 and self.numOfHours != 0):
            if (self.bonusCom != 0):
                return (self.numOfHours * self.hourContract) + self.bonusCom
            elif (self.contractCom != 0 and self.contractNum != 0):
                return (self.numOfHours * self.hourContract) + (self.contractCom * self.contractNum)
            else:
                return self.numOfHours * self.hourContract
        
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')



# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
