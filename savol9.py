a = input().split()
for i in range (0,len(a)-1):
    a = input().split()
cnt=0
for i in range (0,len(a)-1):
    for k in range(0,len(a)-1):
        if int(a[i])==int(a[k]):cnt+=1
        if cnt==0: print(int(a[i]))