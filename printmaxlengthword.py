S=input()
r=S.split()
le1=len(r[0])
le2=len(r[1])
if le1>le2:
	print(r[0])
elif le1==le2:
	print(r[0])
else:
	print(r[1])
