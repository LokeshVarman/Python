N=int(input())
for i in range(1,N-1):
  if N%i==0:
    break
  else:
    print("no")
print("yes")
