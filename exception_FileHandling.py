try:
    filename=input("Enter the file name:")
    file=open(filename,'r')
    number=int(file.readline())
    print("number from file:",number)
    file.close()
except FileNotFoundError:
    print("file does not Exist!!!!")
except ValueError:
    print("file does not have integer")
except :
    print("unknown error")