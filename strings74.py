N=int(input())
s=input()
l=[]
for i in s:
  if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
    s.replace(i,'')
  else:
    l.append(i)
d=l[::-1]
g=''.join(map(str, d))
print(g)

