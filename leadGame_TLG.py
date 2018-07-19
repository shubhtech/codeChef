games =int(raw_input())
record={}
for i in range(games):
    p1= int(raw_input())
    p2= int(raw_input())

    if(p1>p2):
        lead=p1-p2
        winner='Player 1'

    else:
        lead=p2-p1
        winner='Player 2'
    
    #print lead
    #print winner            
    record.update({lead:winner})                       #update dictionary 
#print record                                          #print dictionary 
#print record.keys()                                   # print keys of dictionary
#print max(record.keys())                              #print maxximum value of key of dictionary
print record.get(max(record.keys()))                   #print value belong to the maximum key in dictionary