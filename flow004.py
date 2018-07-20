inputs= int(input())
list1=[]
first_digit=0
last_digit=0
result=0
list2=[]

for i in range(inputs):
  value=int(input())
  list1.append(value)
print (list1)

for i in range(inputs):
  first_digit=int(list1[i])%10
  while int(list1[i])!=0:
    last_digit=int(list1[i])%10
    list1[i]=int(list1[i])/10
  result=first_digit+last_digit
  list2.append(result) 
print (list2)