for i in range(int(input())):
	a = int(input())
	c = 0
	while(a>=0):
		if(a>2):		
			c = c+(a-2)//2
		a = a-2
	print(c)
