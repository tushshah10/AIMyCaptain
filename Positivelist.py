list1=[]
print("enter 10 elements")
for i in range(0,9):
    ele=int(input())
    list1.append(ele)
print("The positive elements are:\n")
for i in list1:
    if (i>0):
        print(i)
        
