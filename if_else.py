import math
try:
    num=int(input("enter a number:"))
    if num<0:
        raise ValueError("negative number.....")
except ValueError:
    print("enter positive number only.....")
else:
    print("SquareRoot:",round(math.sqrt(num),4))