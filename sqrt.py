import math
list=[]
list_2=[]

## 1. take total no. of input

input=int(raw_input())

## 2. take inputs individually

for i in range(input):
    values=raw_input()

## 3. save those inputs in a list individually
    list.append(values)
    
## 4. square-root list elements individually and save results in a list as well

for j in range(input):
    answer=int(math.sqrt(int(list[j])))
    list_2.append(answer)                             #list_2.append(int(math.sqrt(int(list[j])))) 

## 5. print results 
print list_2