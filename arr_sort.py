N=int(input())
arr=[int(x) for x in input().split()]
samp=arr
samp.sort()
if arr==samp:
  print("yes")
else:
  print("no")
