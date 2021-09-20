value = 12 / 3 
print(value)

# module operator is a percent symsbol 

remainder = 13 % 5
print(remainder)


multiline = """
 Hello I \"will back to python
"""

print(multiline)

first = "Nataraj"
Lastname = first + " Hello"

print(Lastname)

# convert integer to string 

age = 34 
age_as_str = str(age) + "hello"

print(age_as_str)

name = "nataraj"
print(f"My name is {name}")

greeting = f"How are you, {name}"
print(greeting)
jose_greeting = greeting.format(name)
print(jose_greeting)

name = "Rolf Smith"
street = "73/1 v.o.c street chidamabaram"
pincode = 608001

combine = f"""
          name :    {name}
          street :  {street}
          pincode : {pincode}

          """
print(combine)
