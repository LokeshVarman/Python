n=int(input())
a=list(map(int,input().split()))
res = max(set(a), key = a.count) 
print(res)
