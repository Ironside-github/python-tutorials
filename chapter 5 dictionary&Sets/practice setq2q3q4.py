#Write a program to enter 8 numbers form the user and display all unique numbers

a= set()
print(type(a))
a1 = int(input("Enter first number :\n"))
a.add(a1)
a2 = int(input("Enter second number :\n"))
a.add(a2)
a3 = int(input("Enter third number :\n"))
a.add(a3)
a4 = int(input("Enter fourth number :\n"))
a.add(a4)
a5 = int(input("Enter fifth number :\n"))
a.add(a5)
a6 = int(input("Enter sixth number :\n"))
a.add(a6)
a7 = int(input("Enter seventh number :\n"))
a.add(a7)
a8 = int(input("Enter eight number :\n"))
a.add(a7)
print("You have entered below values: \n")
print(a)

# To check weather we can add both integer and string value in a set or not,,,,,Yes we can add.
b = {18,"Amit"}
print(type(b))
print(b)

#Adding values to a set and find out their length
s= set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print(s)