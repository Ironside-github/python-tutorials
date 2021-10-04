#problem 2 of practice set
l1=["Amit","Shaurya","Vinay","Anurag","Ajay","Akhilesh","Vijaya"]
for i in l1:
    if i.startswith("A"):
        print("Hello" + i)


#program to print factorial of the given number
n=int(input("Enter the no:"))
fact=1
if n>0:
        for n in range (1,n+1):
            fact= fact*n
        print("The factorial of " + str(n) + "is" + str(fact))
else:
    print("Factorial can't be find out! Enter a new value>0.")


#program to print star pattern
n= int(input("Enter no of lines u want to print star pattern :"))
i=0
for i in range(1 ,n+1):
    print("*" *i)
