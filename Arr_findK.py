n,k=[int(x) for x in input().split()]
a=list(map(int,input().split()))
count=0
for i in a:
  if i==k:
    count+=1
  else:
    pass
print("yes",count)
