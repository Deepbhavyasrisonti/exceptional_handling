try:
    num1=int(input("enter numerator:"))
    num2=int(input("enter denominator:"))
    output=num1/num2
    print("Result:",output)
except ZeroDivisionError:
    print("cannot divide by zero...........")
