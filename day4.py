print("welcome to moon weight calculator")
name=input("whats your name?")
earth_weight=float(input("whats your weight on earth:"))
print("your weight in the different planots are,")

moon_weight=earth_weight*0.165
mars_weight=earth_weight*0.378
jupiter_weight=earth_weight*2.528

print("....result....")
print(f"hey!{name}!")
print(f"in moon:{moon_weight}")
print(f"in mars:{mars_weight}")
print(f"in jupiter:{jupiter_weight}")