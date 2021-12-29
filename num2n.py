
def n2n(num, iters):
    ######## Number to list #######################
    num = str(num) # Number to string ("19264")
    numLi = list(num[:]) # numLi = num in a list ("1","9","2","6","4")
    numLi = [int(x) for x in numLi] # numLi = numLi list with ints  ((1,9,2,6,4))
    ###############################################
    tSum = (sum(numLi)+1)**2  # (23)
    pSum = tSum  # (23)
    ###############################################
    for _ in range(0,iters):
        for x in range(0,len(numLi)):
            numLi[x] = int(str(numLi[x]+pSum)[-1])
            pSum -= numLi[x]
        tSum += sum(numLi)+1
        pSum = tSum
    if (numLi[0] == 0):
        numLi[0] += 1
    num = [str(x) for x in numLi]
    num = int("".join(num))
    return num
'''
#print(n2n(1000000,100))
for x in range(0,100):
    print(str(x) + ". " + str(n2n(999999,x)))
'''