while True:
  accesscode=input()
  if accesscode== "1":
    print("1.BALANCE \n 2.WITHDRAWL \n 3.MINISTATEMENT \n 4.DEPOSIT")
    break
  else:
    print("ACCESS CODE INCORRECT,ENTER AGAIN")
    continue
def balance():
  print("your balance is:",bal)


def deposit():
  new_depo=int(input("Amount to be deposited?"))
  deposit+=new_depo
  depositlist=[]
  depositlist.append(new_depo)
  print("The amount has been added successfully")

def withdrawl():
  minbal=5000
  withamt=int(input("enter withdraw amount")
  if withamt>(balance+minbal):
    bal=balance-withamt

def ministatement():
  print("username:",username)
  print("acc no:",account)
  print("deposit history")
  print(depositlist)
  print("withdrawl list",withdrawlist)
choice=input("Enter your choice:")
if choice=="1":
  bal()
def

