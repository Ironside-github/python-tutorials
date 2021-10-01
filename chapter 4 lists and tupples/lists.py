#use of list and various functions performed in the list

a=[1,45,66,76,50,2,23,42,33,89]
print(a[3])
a.sort()  #sort the given list in ascending order
print(a[0:4])
a.reverse()   #reverse the list
print(a[0:6]) 
a.append(98) #add 98 to the last item of the list
print(a[0:])
a.insert(3,57) #adding item to 3rd index of the list
print(a[0:])
a.pop(3) #removing value at index 3
print(a[0:])
a.remove(42) #removing value42 from the list
print(a[0:])
