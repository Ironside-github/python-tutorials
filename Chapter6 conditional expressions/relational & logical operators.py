# Relatonal operators& logical operators in python--------------------------
# == (equals to)
# >= (greater than equals to)
# <= (less than equals to)
#Logical operators--------------------------------------------------------
# And operator(true if both operand true)
# Or operator (true if atleast one operand is true otherwise false)
# Not Operator(inverts true into false & false into true)

a= int(input("Enter your age :\n"))
if(a>18 and a<60):
    print("You are elligibleto work with us.")
else:
    print("You can't work with us! Please look for some other company")