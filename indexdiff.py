n=int(input())
arr=list(map(int,input().split()))
l=max(arr)
s=min(arr)
la=arr.index(l)
sa=arr.index(s)
print(la-sa)
