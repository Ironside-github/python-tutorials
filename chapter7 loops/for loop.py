#FOR LOOP SYNTAX
#for i in range(1,8,2)1-start 8-stop stepsize-2(after 1 3 comes)/////stepsize usually not used
#else can also be used along with for loop
#break and continue is used along with loops
#pass statement----pass is null statement in python and it instruct to do nothing

a= int(input("Enter any number you want to print its table:"))
m1=1
for m1 in range(1,11):
    mul= a*m1
    print(str(a)+"*" +str(m1) + "=" + str(mul)) #we can use f string as(f"{a}*{m1}={a*m1}")
    if m1 == 11:
        break

