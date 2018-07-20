#1. enter no. of inputs
inputs=int(raw_input())
list=[]
list2=[]
add=0

#2. enter values of inputs and store them in a variable
for i in range (inputs):
    values=raw_input()
    list.append(values)
#print list

#3. find sum of digit for one number and then apply it on list items
for i in range (inputs):
    sum=0
    while (int(list[i]!=0)):
        add= int(list[i])%10
        list[i]=(int(list[i]))/10
        sum=sum+add
    list2.append(sum) 

#4. store results in list and print them
print list2