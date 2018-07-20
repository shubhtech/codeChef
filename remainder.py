#1. enter no. of input pairs
input=int(raw_input())
list1=[]
list2=[]
list3=[]

#2. enter pairs
for i in range(input):
    value1=int(raw_input())
    value2=int(raw_input())
    list1.append(value1)
    list2.append(value2)
#print list1
#print list2
#3. find remainder for one pair and then apply for loop
for i in range(input):
    answer=int(list1[i])%int(list2[i])
    #print answer
#4. store result in list and print result
    list3.append(answer)
print list3
