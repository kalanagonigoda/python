#simple calculator
#this is my first calculator project

print("--my calculator--")

#taking input from user
a=int(input("enter first number"))
b=int(input("enter second number"))

# calclation
print(f"addition: {a+b}")
print(f"subtraction: {a-b}")
print(f"multiplication:{a*b}")
if b!=0:
    print(f"division:{a/b}")
else:
    print("cannot divided by zero")