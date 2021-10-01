#python program to enter name by the user and is followed by good afternoon
a = input("Enter your name")
#print("Good Afternoon " +a)

#program to fillin a letter template with name and date

letter =''' Dear<|NAME|>,
I am happy to inform you on behalf of ABC Coding class.com that
 you are selected!
 greetings from the manager
 Date : <|DATE|>'''
 #x = input("Enter your name\n")
# y = input("Enter date\n")
 letter = letter.replace("<|NAME|>",a)
 letter = letter.replace("<|DATE|>" ,y)
 print(letter)