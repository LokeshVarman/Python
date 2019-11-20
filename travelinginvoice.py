
user_name=input("enter name")
while True:
  emailid=input("enter mail")
  if "@" and "." not in emailid:
    print("Sorry, @ and . are mandatory")
    continue
  else:
     break
while True:
  mobno=input("enter mobno:")
  if len(mobno)!=10:
    print("Sorry, enter 10 numbers")
    continue
  else:
     break
while True:
  source=input("enter strt(kms)")
  if source.isalnum()== True:
    print("Sorry, enter numeric values")
    continue
  if "-" in source:
    print("sorry,enter positive values")
  else:
    break
s=float(source)
while True:
  desti=input("enter des kms")
  d=float(desti)
  if d<s:
    print("destina must me greater than source")
    continue
  if desti.isalnum()== True:
    print("Sorry, enter numeric values")
    continue
  if "-" in desti:
    print("sorry,enter positive values")
  else:
     break
if source!=desti:
  print("Categories.....\n 1.Bike \n 2.Car \n 3.Auto")
  forcar=12
  forbike=5
  forauto=7
  totkms=float(float(desti)-float(source))
  cat=input("enter your choice")
  if cat=="1":
    price=float(totkms*forbike)
    chosen="BIKE"
  if cat=="2":
    price=totkms*forcar
    chosen="CAR"
  if cat=="3":
    price=totkms*forauto
    chosen="AUTO"
  print("INVOICE FOR YOUR TRAVEL")
  print("username:",user_name)
  print("emailid:",emailid)
  print("totalkms:",totkms)
  print("chosen category:",chosen)
  print("TOTAL PRICE:",price)
else:
  print("YOU CANNOT TAKE A RIDE FOR 0 KMS")
