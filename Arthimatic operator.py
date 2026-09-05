#Arthametic operator

a = 10
b = 3 

print("Addition:",a+b)
print("Subtration:",a-b)
print("Muliplication:",a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print("Remainder:",a%b)
print("Power:",a**b)

#Simple caluclators
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Student marks calculator
name = input("Enter student name:")

m1 = int(input("Enter Python marks:"))
m2 = int(input("Enter Java marks:"))
m3 = int(input("Enter SQL marks:"))

total = m1 + m2+ m3
average = total / 3

print("\n----- student Report ------")
print("Name:", name)
print("Total:", total)

#Shopping bill calculator
pricel = floar(input("Enter produt 1 price"))
price2 = float(input("Enter produt 2 price"))
price3 = float(input('Enter produt 3 price'))

total = pricel + price2 + price3

#assignment operators
x = 10

x = 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

#bank balance
balance = 10000

deposit = 5000
balance += deposit

print("After Deposit:", balance)

withdraw = 2000
balance -= withdraw

print("After withdrawal:", balance)

#comparison operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a)


#age eligibility checker
age = int(input("Enter your age:"))

print("Eligibile:", age >= 18)

#pass or fail checker
marks = int(input("Enter marks:"))

print("passed:", marks >= 40)

#login validation
correct_username = "admine"
correct_password = "1234"

username = input("Enter username:")
password = input("Enter password")

print(username == correct_username)
print()
