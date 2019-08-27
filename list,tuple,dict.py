#list
list1=[5,"loki",3,5,6]
list1=tuple(list1)
print(list1)
print(type(list1))
#dictionary
dic={'bike':"ktm" ,'rc':'**','owner':'loki'}
print(dic)
dic['place','pin']= 'vnb'
print(dic)

#listcompre
modern='lokesh'
lis=[s for s in modern if(s=="k")]
print(lis)

#forloop,list to tuple conversion
for s in modern:
    if(s=="k"):
      print(s)

fruit=["lokesh","rasul"]
for i in fruit[:1]:
    print(i)
    
fruit=["lokesh","rasul"]
tup=tuple(fruit)
print(tup)
for i in tup:
    print(i)


tup=(1,2,3)
for i in tup:
    print(i)
