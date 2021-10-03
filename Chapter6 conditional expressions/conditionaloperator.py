#If else &elif condition in python
# Syntax : if(condition1):
#                   expression1
#          elif(condition2):
#                 expression2 //execute if condition 1 false if true exit after executing 1st condition,,,,only one if and else execute 
#          else:
#                default expression
#we can also use multiple if statements


#write a program to printyes when age entered by the user is greater than or equal to 18.

#a= int(input("Enter your age :\n"))
#if(a>=18):
 #   print("yes")
#else:
 #   print("No")

#if-elif-else condition example// In below example if entered value is greater than 30 than it will execute only 1st elif condition and directly jump out of loop
a1= int(input("Enter your age :\n"))
if(a1<30):
    print("Entered number is less than 30")
elif(a1>30):
    print("entered number is greater than 30")
elif(a1>60):
    print("Entered number is greater than  than 60")
else:
    print("Entered number is greater than 60. Please enter number between 0 to 60!")


#multiple if conditions with else condition example
a2= int(input("Enter your age :\n"))
if(a1<30):
    print("Entered number is less than 30")
if(a1>30):
    print("entered number is greater than 30")
if(a1>60):
    print("Entered number is greater than  than 60\n")
else:
    print("\n Entered number is greater than 60. Please enter number between 0 to 60!")

#Is and In condition

a3= None
if(a3 is None):
    print("true")
else:
    print("false")

a4 =[43,34,23,12]
print(143 in a4)


