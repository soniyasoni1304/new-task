# create a list
stationary=["pen","pencil","scale"]
print("The stationary items are:",stationary)

#Acess list element
hardware=["moniter","mouse","keybord"]
print(hardware[1])

#negtive index
hardware=["moniter","mouse","keybord"]
print("The negative index of -1 is:",hardware[-3:-1])

#change element in list
stationary=["pen","pencil","scale"]                
print("original list:",stationary)
stationary[2]="sharpner"                
print("updated list:",stationary)

#del  (remove one or more element from list)
stationary=["pen","pencil","scale"]
del stationary[0]
print("updated list:",stationary)
stationary=["pen","pencil","scale","eraser"]
del stationary[0:1]
print("updated list:",stationary)
#len()  ("find total no.of element in list")
stationary=["pen","pencil","scale","eraser","eraser"]
print("total elements:",len(stationary))
#for loop  (iterating through list)
stationary=["pen","pencil","scale","eraser"]
for item in stationary:
    print(item)
#1.index()  (find index of element)
stationary=["pen","pencil","scale","eraser"]
x=stationary.index('pen')
print("pen index is :",x)
#2.append() (add a element end of the list)
stationary=["pen","pencil","scale"]                
print("original list:",stationary)
stationary.append("Eraser")                  
print("updated list:",stationary)
#append() (adding list into a list)
stationary=["pen","pencil","scale"]                
print("original list:",stationary)
stationary1=["eraser","sharpner"]
stationary.append(stationary1)                  
print("updated list:",stationary)
#3.extend() (add all the item for specified iterable)
stationary=["pen","pencil","scale"]
stationary1=["eraser","sharpner"]
stationary1.extend(stationary)
print("new list:",stationary1)
#4.insert()  (add a element specified index of the list)
stationary=["pen","pencil","scale"]                
print("original list:",stationary)
stationary.insert(1,"Eraser")                  
print("updated list:",stationary)
#5.remove()  (remove an element from the list)
stationary=["pen","pencil","scale"]                
stationary.remove("pencil")
print("updated list:",stationary)
#6.count()  (returns the no.of times specified element appears in list)
stationary=["pen","pencil","scale","pencil","sharpner","pencil"]
x=stationary.count("pencil")
print("count repeated times:",x)
#7.pop()  (remove the item at specify index)
stationary=["pen","pencil","scale"]
x=stationary.pop(0)
print("removed element:",x)
#8.reverse()  (reverses the elements of the list)
stationary=["pen","pencil","scale"]
stationary.reverse()
print("reversed list is:",stationary)
# reversed a list using slicing operator
stationary=["pen","pencil","scale"]
x=stationary[::-1]
print("reversed_list:",x)
#9.sort()  (sort the elements in list)
num=[1,5,9,7,2]
num.sort()
print("sorted list is:",num)
#10.copy()   (returns a shallow copy of list)
stationary=["pen","pencil","scale"]
x=stationary.copy()
print("copied list is:",x)
#11.clear()   (remove all the items in list)
stationary=["pen","pencil","scale"]
stationary.clear()
print("list after clear:",stationary)
#list comprehension  (create a new list based on the values of existing list)
numbers=[1,2,3,4]
doubled_numbers=[num*2 for num in numbers]
print("doubled num is:",doubled_numbers)
