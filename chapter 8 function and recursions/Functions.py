#program to find maximum no among three numbers

def maximum(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print("number1 is the greatest. The no is: ",num1)
    elif(num2>num1 and num2>num3):
        print("number 2 is the greatest. The no is:", num2)
    else:
        print("number3 is the greatest. The no is:",num3)

num1= int(input("Enter number 1:"))
num2= int(input("Enter number 2:"))
num3= int(input("Enter number 3:"))

maximum(num1,num2,num3)

#Program to convert enter temperature from degree to farenheight
