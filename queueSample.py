import queue

L = queue.Queue(maxsize=10)

L.put(1)
L.put(2)
L.put(3)
L.put(4)
L.put(5)

L.put(6)
L.put(7)
L.put(8)
L.put(9)
L.put(10)

#for elem in list(L.queue):
    #print(elem)

if L.full:
    L.get()
    L.put(11)
#L.put(12)
#L.put(13)


#for elem in list(L.queue):
    #print(elem)

LofQ = list(L.queue)
#print(LofQ[0]) 

IGreater = 0 
for k in range(0,len(LofQ),1):
    #print(LofQ[k])
    if k!=len(LofQ)-1:
        if LofQ[k]<LofQ[k+1]:
            IGreater=IGreater+1
    if k==len(LofQ)-1:
        if LofQ[k-1]<LofQ[k]:
            IGreater=IGreater+1

print(IGreater)








