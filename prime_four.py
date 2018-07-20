inputs=int(input())
list1=[]
list2=[]
count=0

for i in range(inputs):
  value=int(input())
  list1.append(value)
#print (list1)

for i in range(inputs):
  while(list1[i]!=0):
    remainder=int(list1[i])%10    
    (list1[i]) = (list1[i])/10    
    if(remainder==4):
      count=count+1      
    else:
      continue
  list2.append(count)
print (list2) 