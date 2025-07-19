import datetime
try:
    x=int(input("enter num:"))
    y=int(input("enter num:"))
    print("result:",x/y)
except (ZeroDivisionError,ValueError,TypeError,StopIteration,NameError) as e:
    ct=datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    txt=f"[{ct} Error: {type(e)}]\n"
    with open ("data.txt",'a') as file:
        file.write(txt)