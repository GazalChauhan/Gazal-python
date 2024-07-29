# Python program for simple calculator
# Function for adding two numbers
def add(num1 , num2):
    return num1 + num2
# Function  for substract two numbers
def substract(num1 , num2):
    return num1 - num2
# Function for multiply two numbers
def multiply(num1 , num2):
    return num1 * num2
# Function to divide two numbers
def divide(num1 , num2):
    return num1 / num2

print("please select operation \n" \
      "1. Add\n" \
      "2. substract\n" \
      "3. multiply\n" \
      "4. divide\n")

#Take input from  user
select = int(input("select operation from 1, 2, 3, 4 :"))

number_1= int(input("enter first number :"))
number_2= int(input("enter second number :"))

if select == 1:
    print( number_1, "+",  number_2, "=" , add(number_1, number_2))
elif select ==2:
    print( number_1, "-", number_2, "=", substract(number_1, number_2))
elif select ==3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2) )
elif select ==4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
else:
    print("invalid ")


    