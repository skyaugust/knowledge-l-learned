
def fun(cores):
    minnums = max(2, min(cores -1 ,4))
    maxnums = cores*2 + 1
    return (minnums, maxnums)

for i in range(1, 9):
    print str(i)+'|'+ str(fun(i)[0])+'|'+ str(fun(i)[1]) 