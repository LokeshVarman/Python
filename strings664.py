s=input()
s=s.split()
l=[]
for i in range(len(s)):
    if i%2==0:
        d=s[i].upper()
        l.append(d)
    else:
        d=s[i].lower()
        l.append(d)
print(*l)
