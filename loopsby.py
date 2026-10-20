print("my loop learning")
print("pro1,sum calculator")
total = 0
for i in range(1,11):
    total +=i
print(f"adding{i},total now:{total}")
print(f"final sum of 1 to 10={total}")

print("pro2,mutiplication table")
num =int(input("put any number"))
print(f"\n{num} table:")

for i in range(1,11):
    print(f"{num*i}")

    print("pro3,countdown")
    count=5
    while count > 0 :
        print(count)
        count -= 1
        print("hellow new year!")