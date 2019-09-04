N=int(input())
L,R=[int(x) for x in input().split()]
C=[i for i in range(L,R)]
if N in C:
	print("yes")
else:
	print("no")
