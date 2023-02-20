import operators
import others
import  trigs

#x = others.cube(9)
#print(x)
#y = operators.add(88,99)
#print(y)
operator = input("enter operator:")
if operator == "cube":
    number = eval(input("enter number"))
    x = others.cube(number)
    print(x)
elif operator == "sin":
    angle = eval(input("enter angle in degrees:"))
    sin_of_angle = trigs.get_sine(angle)
    print(sin_of_angle)
elif operator == "tan":
    angle = eval(input("enter a number:"))
    print(trigs.get_tan(angle))
elif operator == "cos":
    angle = eval(input("enter a number:"))
    print(trigs.get_cos(angle))

else:
    num1 = eval(input("enter number1:"))
    num2 = eval(input("enter number2:"))
    if operator == "+":
        x = operators.add(num1,num2)
        print(x)
    elif operator == "-":
        x = operators.subtract(num1,num2)
        print(x)
    elif operator == "*" or "x" or "X":
        x = operators.multiply(num1,num2)
        print(x)
    elif operator == "/":
        x = operators.divide(num1,num2)
        print(x)
