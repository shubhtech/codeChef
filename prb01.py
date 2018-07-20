cases=int(input())
list1=[]
for i in range(cases):
  ids=input()
  list1.append(ids)
for i in range(cases):
  if(list1[i]=='B' or list1[i]=='b'):
    print("BattleShip")
  if(list1[i]=='C' or list1[i]=='c'):
    print("Cruiser")
  if(list1[i]=='D' or list1[i]=='d'):
    print("Destroyer")
  if(list1[i]=='F' or list1[i]=='f'):
    print("Frigate")
  else:
    continue
