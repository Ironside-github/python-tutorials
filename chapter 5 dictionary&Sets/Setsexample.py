#Use of Set along with example
# Set is a collection of non repititive elements./Unordered and unindex/ Bo way to change items in sets/can't contain duplicate values
#defining a set-----first way
a={1,2,3,4,1}
print(type(a))
#defining a set -----second way
b=()
print(type(b)) #Here the type is tupple
c= set()
print(type(c)) #Here the type is set
#Adding data to the set manually
c.add(2)
c.add(1)
c.add(1)
c.add(4)
c.add(5)
c.add(6)
print(c) # Here we can see that any repetion of values ignored by the set

#We can't add dictionaries and list into the set,,,,,,lets try-----because dictionary and lists are not hashable means items can be changed
#c. add({4:5})

#We can add tupple to SET because it is also hashable ie can't contain repetitive elements
c. add((6,8,9,0,1,2,3,4))
print(c) 

# Functions which can be performed in SETS
#FUN1. Len()------print the length of a SET
print(len(a))
print(len(c))   

#FUN2 remove()-----to remove a value from the set
a.remove(1)
print(a)
a. add(1)
print(a)
#a.remove(15)--------throw an error for every value enered which is not present in the set.
 
#FUN3 pop()-----removing one element from the set starting from first element
print(a)
a.pop()
print(a)

#FUN4 clear()-------clear whole set ie delete all elements from the set
a. add(1)
#FUN5 Union()--------return all the values of two sets between which union function is used.
print(a.union({9,11}))


#FUN6 intersection()-----return common values in between sets
print(a.intersection({3,4}))
 


