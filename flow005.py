list=[100,50,10,5,2,1]

for i in range(int(input())):
n = int(input())
  x=0
  r=0
  for j in list:
    x=n//j
    r=r+x
    n=n%j
  print (r)
