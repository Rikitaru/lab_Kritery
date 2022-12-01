import random
from numpy import std
N = 6
mylist = [0,0,0,1,1]
zerolist = []
onelist = []
countList= []
for i in range(0, N):
    zerolist.append(0)
    onelist.append(0)
    mylist.append(random.randint(0,1))
    if mylist[i] == 1:
        onelist[0]=onelist[0]+1
    else:
        zerolist[0]=zerolist[0]+1
print(mylist)
#print("zero = "+ str(zerolist[0]/N*100) + "% one = "+ str(onelist[0]/N*100) + "%")
countList.append(N)



check = True
last = True
tempList=[]
for vichet in range(1, N):
    for j in range(0, N - vichet):
        for m in range(j, j + vichet + 1):
            tempList.append(mylist[m])
        print(tempList)
        for r in range(1, vichet+1):
            if tempList[0] != tempList[r]:
                break
            if r == vichet and tempList[0] == 0:
                zerolist[vichet]= zerolist[vichet] + 1
            elif r == vichet and tempList[0] == 1:
                onelist[vichet] = onelist[vichet] + 1
        #print("zerolist= ", zerolist)
        #print("onelist= ", onelist)
        tempList.clear()
    countList.append(N - vichet)
#print("countList= ",countList)
#print("zerolist= ",zerolist)
#print("onelist= ",onelist)
for i in range(0, N):
    print("0"*(i+1), str(round(zerolist[i] / countList[i] * 100)) + "%")
    print("1"*(i+1), str(round(onelist[i] / countList[i] * 100)) + "%")
#print("countList= ",countList)
#print("zerolist= ",zerolist)
#print("onelist= ",onelist)
