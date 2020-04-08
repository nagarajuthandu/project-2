size=int(input("Enter the size of the list"))
l=[]
secondMax=0
for i in range(0,size):
    l.append(int(input()))
for i in range(0,size):
    if(l[i]<max(l) and l[i]>secondMax):
             secondMax=l[i]

print("Second max:"+str(secondMax))
