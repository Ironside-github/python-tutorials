#Program to find out the percent marks entered by the user and grade them accordingly

m1= int(input("Enter the marks for subject1="))
m2= int(input("Enter the marks for subject2="))
m3= int(input("Enter the marks for subject3="))
m4= int(input("Enter the marks for subject4="))
m5= int(input("Enter the marks for subject5="))
m6= int(input("Enter the marks for subject6="))
m7= int(input("Enter the marks for subject7="))
per = (m1+m2+m3+m4+m5+m6+m7)/7
if(per>=90 and per<=100):
    print("Congratulations Grade of the student is Excellent!")
elif(per<90 and per>=80):
    print("Grade of the student is A.")
elif(per<80 and per>=70):
    print("Grade of the student is B.")
elif(per<70 and per>=60):
    print("Grade of the student is C.")
elif(per<60 and per>=50):
    print("Grade of the student is D.")
elif(per<50 and per>=40):
    print("Grade of the student is E.")
else:
    print("Student is fail in the exams.")