cases=int(input())
list1=[]
list2=[]
list3=[]


for i in range(cases):
  times=int(input())
  limit=int(input())
  loop=times*limit
  #list1.append(times)
  #list2.append(limit)
  list3.append(loop)

for i in range(len(list3)):
  answer=0
  for j in range(0,int(list3[i]+1)):
    answer=answer+j
  list1.append(answer)
print (list1)
