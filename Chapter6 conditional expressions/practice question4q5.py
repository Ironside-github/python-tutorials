#Program to count no of characters in ausername enteredby the user.
a= input("Enter the user name :")
a1 = len(a)
if(a1>10):
    print("Entered Username is more than 10 characters.!",a1)
else:
    print("Entered Username is less than 10 characters and within the range!", a1)

#program to find out weather aname is in the list or not
list1= {"Amit","garima","vishal","krish","justice"}
a= input("Enter the name you want to search in the list :")
if a in list1:
    print("Hurray! Name entered by the user fount in the list.")
else:
    print("Entered name by the user is not in the list.")