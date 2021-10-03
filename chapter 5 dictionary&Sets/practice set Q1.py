#Write a program to create a hindi dictionary containing few words and display its english meaning as value entered by the user.

hindidict ={
    "darwaja" :"door",
    "khidki" : "window",
    "chaku" : "knife",
    "pathar" :"stone",
    "mopat" :"motorcycle"
}
a= input("Enter the world you want to know its english translation :\n")
print("The English translation of your entered word is:" , hindidict.get(a))
print("Thanku for using hindi dictionary!!!")
