#create a function  (only run when it's called)
# def student(name):
#     print("name:", name)

# student("mani")
#arguments
#1.positionl arguments  (corresponding position)
# def add(a,b):
#     print("Addition of a and b is:",a+b)

# add(3,5)

#2.keyword Arguments   (position doesn't matter)
# def sub(a,b):
#     print("Subtrction of a and b is",a-b)

# sub(b=2,a=5)

#3.Default Arguments
# def mul(a,b=5):
#     print("multiplication of a and b is:" ,a*b)

# mul(2)

#4.Arbitary positionl arguments
# def add_all(*numbers):
#     return sum(numbers)
# print(add_all(2,4,7,5))

#5.Arbitary keyword arguments
# def sample(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)

# sample(name="siva",age=10,gender="male")

# ##pass
# def future_function():
#     pass

##return
# def find_squre(num):
#     result= num*num
#     return result
# square=find_squre(3)
# print("square of 3 is:",square)

# #lambda   (no.of arg but one exp)
# x=lambda x,y:x+y
# print(x(2,3))

# #lambda function
# greet=lambda:print("hello")
# greet()
# def greet(name):
#     return lambda x : print("welcome",name)

# x=greet("siva")


#scope of variable
#local variable  (declare inside fun, cannot access outside fun)
# def greet():
#     message="Hello"
#     print(message)
# greet()

#Global varible   (declare outside fun,access both in & outside fun)
# message="Hello"
# def greet():
#     print("local",message)
# greet()
# print("Global",message)

#Global keyword   (change the message)
# x=300
# def num():
#     global x
#     x=200
# num()
# print(x)

#nonlocal variable (inside nested fun)
#outside function
def outer():
    message="local"
    #nested function
    def inner():
        #declare nonlocal variable
        nonlocal message
        message="nonlocal"
        print("inner",message)
    inner()
    print("outer",message)
outer()
