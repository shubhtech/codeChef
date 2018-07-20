no_of_sets=int(input())
list1=[]
list3=[]

for i in range(no_of_sets):
  list1.append([])      #create nested list
  list2=[]               
  for j in range(0,3):
    values=int(input())            #enter values in nested lists
    list2.append(values)
    list2.sort() 
  list3.append(list2[1])       #make a list of 2nd largest list
  print("\n")
print(list3)