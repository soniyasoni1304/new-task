def second_largest(num):
    large=max(num)
    num.remove(large)
    return max(num)
num=[1,2,3,4,5]
second_larg=second_largest(num)
print("The second largest unique number is : ",second_larg)
