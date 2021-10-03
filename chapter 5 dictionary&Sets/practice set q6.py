#Write a program to create a dictionary and allow ur friends to add their favourite langyages and assume mane of friend as unique

langdict = {}
print(type(langdict))
a=input("Enter your favourite language Amit:\n")
b=input("Enter your favourite language Harshit:\n")
c=input("Enter your favourite language Gaurav:\n")
d=input("Enter your favourite language Aman:\n")
e=input("Enter your favourite language Sorabh:\n")
langdict['Amit'] =a
langdict['Harshit'] =b
langdict['Gaurav'] =c
langdict['Aman'] =d
langdict['Sorabh'] =e
print(langdict)
#If the names of two friends are same then the last updated value will be the final value