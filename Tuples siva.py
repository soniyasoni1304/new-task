# #creation of Tuple
# x=("apple","orange","banana","nuts")
# print("The list are:",x)
# #create an single element
# x=("apple")
# print(type(x))
# #Type of value
# x=("apple",)
# print(type(x))

# t1=("apple","banana","orange")
# t2=(1,2,3,4)
# t3=(True,False,True)

# print(type(t1))
# print(type(t2))
# print(type(t3))
# #Index of the value:
# x=("apple","orange","banana","nuts")
# print(x[2])
# #Negative index value:
# x=("apple","orange","banana","nuts")
# print(x[-3])
#Range of negative index 
# x=("apple","orange","banana","nuts")
# print(x[-3:-1])
# # length of the tuple
# x=("apple","orange","banana","nuts")
# print(len(x))

# # Iterate through a tuple
# x=("apple","orange","banana","nuts")
# if "orange" in x:
#     print("yes,'orange is in x")

# #Change tuple values:
# x=("apple","orange","cherry","banana","mango")
# y=list(x)
# y[2]="kiwi"
# x=tuple(y)
# print(x)

# #append the values in tuple
# x=("apple","orange","cherry","banana","mango")
y=list(x)
y.append("kiwi")
x=tuple(y)
print(x)

x=("a","b","c")
y=list(x)
x.append("d")
x=tuple(y)
print(x)

# # Join tuple
# t1=("a","b","c")
# t2=(1,2,3)
# t3=t1+t2
# print(t3)


# # count of tuples
# x=("apple","orange","cherry","banana","cherry","mango")
# y=x.count("cherry")
# print(y)

#Loop Tuples
# x=("apple","orange","banana","nuts")
# i=0
# while i<len(x):
#     print(x[i])
#     i=i+1

# x=("apple","orange","cherry","banana","mango")
# y=list(x)
# y.remove("cherry")
# x=tuple(y)
# print(x)