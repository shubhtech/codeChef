#1.enter n numbers
list=[]
list2=[]
#factorial=1
input=int(raw_input())

#2.input n numbers and store them in a list
for i in range(input):
    value=raw_input()
    list.append(value)

#3.find factorial of a number and put it in a loop
for i in range(len(list)):
    factorial=1
    if int(list[i]) < 0:
        factorial=0
    elif int(list[i]) == 0:
        factorial=1
    else:
       for j in range(1,int(list[i]) + 1):
           factorial = factorial*j

#4.store result in list and print it.    
    list2.append(factorial)
print list2