cases=int(input())
list1=[]

for i in range(cases):
weapons=int(input())
list1.append(weapons)

odd=0
even=0

for i in range(cases):
if(list1[i]%2==0):
even=even+1
else:
odd=odd+1

if(odd>even):
print("NO")
else:
print("YES")
