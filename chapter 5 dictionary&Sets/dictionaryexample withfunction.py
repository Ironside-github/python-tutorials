#use of dictionary along with its functions

myfirstdict = {
    "Name" : "My name is ABC.com",
    "Occupation" : "Buisness",
    "a":[1,4,5,7,8],
    4 : 485
    #myseconddirec = {"harry" : "He is a gud coder for the company"}
}

#Use of various function in the directories which we can perform in python.
print(myfirstdict.items()) #displaying items of the dictionary
print(myfirstdict.values()) #displaying values of the dictionary
print(list(myfirstdict.keys())) #return a list containing all the keys of the dictionary
print(myfirstdict)
updatedict = {"city" : "I lives in Bhubhaneshwar",
              "State" : "Himachal Pradesh",
              "b":[23,45,12,46,78]
}
myfirstdict.update(updatedict) #function update the current dictionary with the new values added by the user
print(myfirstdict) #updated dictionary printed
print("\nupdated keys :")
print(myfirstdict.keys())
print("\nupdated items:")
print(myfirstdict.items())
print(myfirstdict.get("Name1")) #Get function return none if the key is not present in the directory.
#print(myfirstdict["Name1"]) #If we use this method then it will throw error if the key is not present in the dictionary.
print(myfirstdict.get("Name"))
myfirstdict.popitem() #Removes the last inserted item while if we use pop function it will delete selected key value pair
print(myfirstdict)
updatedirct1 ={
    "b1" :[34,56,78,90,12,45,66],
    "Pin code":"174021"
}
myfirstdict.update(updatedirct1)
print(myfirstdict)