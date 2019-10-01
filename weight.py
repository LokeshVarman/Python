s=input()
s=list(s)
ele=0
total=0
for i in s:  
  p=[ord(x) for x in s ]
  while(ele < len(p)): 
    total = total + p[ele] 
    ele += 1
print(total)
