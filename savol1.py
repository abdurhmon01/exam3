a = input().split()
c = -9999999999
for i in a:
    b = len(i)
    if b>=c: c=b
print(c)