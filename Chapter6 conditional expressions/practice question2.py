#Write a program to find out weather a student is pass or fail,if it requires total 40% and at least33%,in each subject to pass
#Assume 3 subjectsand take marks as input from the user.

m1= int(input("Enter marks in first subject :"))
m2= int(input("Enter marks in second subject:"))
m3= int(input("Enter marks in third subject :"))
m4= int(input("Enter marks in fourth subject :"))

if(m1>33 and m2>33 and m3>33 and m4>33 ):
    per= (m1+m2+m3+m4)/4
    if(per> 40):
        print("Congrats !Student has passed with pecentage",per)
    else:
        print("Student is fail because percentage is less than 40.")
else:
    print("You are fail! You have scored less than 33 marks in each subject. Please reappear in the exam")

