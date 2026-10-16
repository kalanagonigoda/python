#smart calculator with user choice 
print("my smart calculator")
#get numbers

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))

#show menu

print("1-addition")
print("2-subtraction")
print("3-multiplication")
print("4-division")

#get choice
choice=int(input("enter your choice(1-4):"))

#logic with else if
if choice==1:
    print(f"result:{a+b}")
elif choice==2:
    print(f"result:{a-b}")
elif choice==3:
    print(f"result:{a*b}")
elif choice==4:
    if b!=0:
        print(f"result:{a/b}")
    else:
        print("error:cannot divided by zero")
else:
    print("invalid choice!enter again")