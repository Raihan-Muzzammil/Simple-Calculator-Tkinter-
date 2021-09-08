import sys

print("Simple Calculator\n")
def sum (a,b):
    return a + b
def sub (a,b):
    return a - b
def mul (a,b):
    return a * b
def div (a,b):
    return a / b

print("1. Addition. \n 2. Subtraction. \n 3. Multiplication. \n 4. Division. \n")

while True:
 choice = input("Enter you choice from the above options : ")
 a = float(input("Enter the first number : "))
 b = float(input("Enter the second number : "))
 if choice in ('1','2','3','4') :
     if choice == '1':
         print("\nAddition\n")
         print(a,"+",b,"=",sum(a,b))
     elif choice == '2':
         print("\nSubtraction\n")
         print(a, "-", b, "=", sub(a,b))
     elif choice == '3':
         print("\nMultiplication\n")
         print(a, "x", b, "=", mul(a,b))
     elif choice == '4':
         print("\nDivision\n")
         print(a, "/", b, "=", div(a,b))
     break
 else:
     print("Enter a valid choice dumbass !")
sys.exit()