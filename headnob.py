cases=int(input())
list1=[]
list3=[]

for i in range(cases):
  nods=int(input("nods"))
  list1.append(nods)
  list1.append([])
  list2=[]
  for j in range(nods):
    head=input()
    list2.append(head)
    count=0
    not_indian=0
    indian=0
  for j in range(nods):
    if(list2[j]=='y'):
      not_indian=not_indian+1
      list3.append("f")
      break
    if(list2[j]=='i'):
      indian=indian+1
      list3.append("i")
      break
    else:
      count=count+1
      continue

  if(indian==0 and not_indian==0):
    list3.append("n")

print(list3)

for i in range(len(list3)):
  if(list3[i]=='i'):
    print("INDIAN")
    continue
  if(list3[i]=='f'):
    print("not indian")
  if(list3[i]=='n'):
    print("not sure")
    continue
  else:
    continue