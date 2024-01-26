list1=map(int,input().split())
listans=[]
for item in list1:
    if item%2==0:
        if (item**2)%3!=0:
            listans.append(item)
    else:
        listans.append()