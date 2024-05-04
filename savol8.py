a = input().split()
cnt=0
for i in range (0,len(a)-1):
    for k in range(0,len(a)-1):
        if int(a[i])!=int(a[k]):cnt+=1
print(cnt)