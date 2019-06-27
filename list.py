#finding the largest number for list

numbers = [1,5,7,3,8]

max = numbers[0]

for number in numbers:
    if max > number:
        max = number
print(number)


#making 2D list

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix: #this will loop rows
    for item in row: #this will loop item from the current row
     print(item) #this will print single element of 2D list e.g : 2


numberList = [2,4,7,9,2,32,6]
numberList.append(56) #append function is use to ADD element at the END
print(numberList)

numberList.insert(0, 34) #INSERT function is use to insert element at the desired location insert(index,element)
print(numberList)

numberList.remove(32) #REMOVE is use to delete element from the list Syntax : list_name.remove(element)
print(numberList)

#numberList.clear() #CLEAR will empty the list
numberList.pop() #this will delete last element of the list
print(numberList.index(7))
print(numberList)

print(numberList.count(2))#this will return the count of 2 from the list

numberList.sort() # SORT the list elements in ascending order
numberList.reverse() #this will SORT list in decending order
print(numberList)


#program to remove duplicates from list

lists = [3,4,6,76,7,7,8,3,]

uniques = []

for list in lists:
    if list not in uniques: #if not present in unqiue list the add it otherwise ignore
        uniques.append(list)
print(uniques)


