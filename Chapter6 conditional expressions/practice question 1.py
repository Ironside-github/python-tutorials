# Program to find out greatest no among four number entered by the user.

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))
d= int(input(" Enter fourth number:"))
if(a>b and a>c and a>d):
    print("Greatest number is a :",a)
elif(b>a and b>c and b>d):
    print("Greatest no is b:",b)
elif(c>a and c>b and c>d):
    print("Greatest number is c:",c)
else:
    print("Greatest number is d:",d)