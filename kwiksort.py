import random,time

from DesmosKiller import main

ktime = 0
itime = 0
kVals = []
iVals = []

def ks(eray):
    if len(eray) < 2:
        return eray
    pivot = eray[len(eray) // 2]
    left = [x for x in eray if x < pivot]
    midul = [x for x in eray if x == pivot]
    right = [x for x in eray if x > pivot]
    return ks(left) + midul + ks(right)

def ins(eray):
    for currentIndex in range(len(eray)):
        smallestIndex = currentIndex
        for j in range(currentIndex,len(eray),1):
            if eray[smallestIndex] > eray[j]:
                smallestIndex = j
        temp = eray[smallestIndex]
        eray[smallestIndex] = eray[currentIndex]
        eray[currentIndex] = temp

repeats = 1
domainMax = 1000
for arrLen in range(0,domainMax+1,1):
    for carrier in range(repeats):
        aray = [x for x in range(arrLen)]
        random.shuffle(aray)
        start = time.time()
        ks(aray)
        end = time.time()
        ktime += end - start
        start = time.time()
        ins(aray)
        end = time.time()
        itime += end - start
    kavg = (ktime / repeats) * (10**6)
    iavg = (itime / repeats) * (10**6)
    kVals.append(kavg)
    iVals.append(iavg)


main.generate_array_then_graph(None,kVals)
main.graph(None,iVals)
main.show()
