# Check whether a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

# Check whether a person is eligible to vote

n = int(input("Enter your age: "))

if n >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#Find the greatest among 3 numbers.
num1=int(input("Enter first number:"))
num2 =int(input("Enter second number:"))
num3=int(input("Enter third number"))
if num1>num2 and num1>num3:
    print(num1,"is greatest")
elif num2>num1 and num2>num3:
    print(num2,"is greates")
else:
    print(num3,"is greatest")

#Check whether a year is leap year.
year = int(input("enter a year:"))
if (year % 4 == 0 and year % 100 !=0 or year % 100 == 0):
    print(year,"is a leap year") 
else:
    print(year,"is not a leap year")

#Check whether a number is positive, negative, or zero.
num = float(input("enter a number:"))
if num >0:
    print("positive")
elif num <0:
    print("negative")
else:
    print("zero")
    # Simple Calculator using if-else

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

print("Result:")

if op == "+":
    print(a + b)

elif op == "-":
    print(a - b)

elif op == "*":
    print(a * b)

elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Division by zero is not allowed")

else:
    print("Invalid operator")

# Print grade based on marks

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")

else:
    print("Grade D")


#Check whether a character is vowel or consonant.
a = input("enter a character:")
if a in ('a','e','i','o','u'):
    print("vowel")
else:
    print("consonant")


#Check whether a number is divisible by 5 and 11.
a = int(input("enter a number:"))
if a%5==0 and a%11==0:
    print("number is divisible by 5 and 11")
else:
    print("number is not divisible by 5 and 11")


# Find smallest among 3 numbers

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a < b and a < c:
    print("Smallest number is", a)

elif b < a and b < c:
    print("Smallest number is", b)

else:
    print("Smallest number is", c)



