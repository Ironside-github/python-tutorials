#Program to convert enter temperature from degree to farenheight

def tempconvert(a):
        f=0
        f=((a * 9/5) + 32)
        print("Temperature in farenheit is :" + str(f)+"f")
        #return()

a= int(input("Enter temperature in degree:"))
tempconvert(a)
