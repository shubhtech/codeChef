cases=int(input())
list1=[]
list3=[]
for i in range(cases):
  values=int(input("no of inputs"))
  list1.append(values)
  list2=[]
  answer=0
  for j in range(int(values)):
    elements=int(input())
    list2.append(elements)
    list2.sort()
  answer=list2[0]+list2[1]
  list3.append(answer)
print(list3)
