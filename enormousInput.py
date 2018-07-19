inputs=int(raw_input())
diviser=int(raw_input())

element_list=[]
k=0
if(inputs<=1000000000 and diviser<=10000000):
    for i in range(inputs):
        element = int(raw_input())
        element_list.append(element)
    
    for j in range(len(element_list)):
        if(element_list[j]%diviser==0 ):
            k=k+1
    print k 
              
else:
    print "wrong"            