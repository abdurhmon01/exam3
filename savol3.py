a = input().split()
c = 99999999999
for i in range (0,len(a)-1):
    if int(a[i])%2!=0: b=int(a[i])
    if b<=c: c=b
print(c)
