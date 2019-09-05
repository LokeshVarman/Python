n=int(input())
arr = list(map(int, input().split()))
a=arr[0]
for i in range(n):
	a&=arr[i]
print(a)
