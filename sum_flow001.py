counts = raw_input()
result=[]
for i in range(int(counts)):
    first = raw_input()
    second = raw_input()
    f=float(first)
    s=float(second)
    result.append(f+s)   #to add element in list
print counts
print('\n'.join(map(str, result)))       #to print elements of a list in saperate line   

