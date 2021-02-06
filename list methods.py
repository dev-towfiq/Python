#list
numbers=[1,2,3,4,5]
print(numbers)
#add an item end of the list
numbers.append(6)
print(numbers)

#insert an item in any index of the list
numbers.insert(0,1) #Here, index[0], value=1  
print(numbers)
#Check if the item is in the list or not
print("6 is in the list:",6 in numbers)

#remove an item from the list
numbers.remove(5)
print(numbers)
#Check if 5 is in the list or not 
print("5 is in the list:", 5 in numbers)

#list length
print("List Length is:",len(numbers))

#Clear the list
numbers.clear()
print(numbers)

#list length
print("List Length is:",len(numbers))