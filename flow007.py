inputs=int(input())
list1=[]
list2=[]

for i in range(inputs):
values=int(input())
list1.append(values)

for i in range(inputs):
reverse=0
while(list1[i]>0):
remainder=int(list1[i])%10
reverse=(reverse*10)+remainder
list1[i]=list1[i]//10
list2.append(reverse)
print(list2)
