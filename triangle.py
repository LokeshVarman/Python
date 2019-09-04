a, b, c = [int(x) for x in input().split()]
if a + b > c or b + c > a or a + c > b:
    print("yes")
else:
    print("no")
