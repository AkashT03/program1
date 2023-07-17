class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        if self.b !=0:
            return self.a/self.b
        else:
            return"Error:Division by zero is not allowed "
a=float(input("ENTER THE FIRST NUMBER :"))
b=float(input("ENETR THE SECOND NUMBER :"))
calculator= Calculator(a,b)
operation=input("ENTER THE TYPE OF OPERATION (add/subtract/multiply/divide):")
if operation =="add":
    result=calculator.add()
    print("Result",result)
elif operation == "subtract":
    result = calculator.subtract()
    print("Result", result)
elif operation == "multiply":
    result = calculator.multiply()
    print("Result", result)
elif operation == "divide":
    result = calculator.divide()
    print("Result", result)
else:
    print("Invalid operation.")
