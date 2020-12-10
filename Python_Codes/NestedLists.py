n = int(input())
list1=[]
list2=[]
dup=[]
for i in range (n):
    list1.append(input())
    A=float(input())
    list2.append(A)
    dup.append(A)
m=min(list2)
list2.sort()
for i in list2:
    if i==m:
        continue
    else:
        m=i
        break
list3=[]
count=0
for i in dup:
    if i==m:
        list3.append(list1[count])
    count+=1
list3.sort()
for i in list3:
    print(i)
