############ NESTED FOR LOOP USING BREAK & CONTINUE ########
number_1=[10,20,30,15]
number_2=[20,40,50]
for x in number_1:
    for y in number_2:
       if x==y:
        print("match found")
        break
       elif x<=y:
         print(x,y)  
         continue
print("end")