try:
    num=int(input("ener a number:"))
    print(num**3)
except (KeyboardInterrupt,ValueError,TypeError):
    print("please check before executing....")
print("Program Terminated")