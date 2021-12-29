def b2b(n, inBase, fiBase):
    n = str(n)
    if (inBase<=24):
        inBaseStr = "0123456789ABCDEFGHIJKLMN"
    else:
        inBaseStr = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    if (fiBase<=24):
        fiBaseStr = "0123456789ABCDEFGHIJKLMN"
    else:
        fiBaseStr = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    # from base to decimal >("A32", base 58)
    num = 0
    for x in range(0,len(n)):
        if (inBaseStr.index(n[x])>=inBase): # if inBase==10 -> A32 can't be base 10
            return "\nError\n"
        num += inBase**(len(n)-x-1)*inBaseStr.index(n[x])  # >(58**(3-0-1) * inBaseStr.index("A") -> 58**2 * 10) >(58**2 * 10 + 58*2 + 1 = 3481)

    # from decimal to base >(8 to base 2) >(9 to base 4)
    if num == 0:
        return "0"
    digits = []
    while num:
        digits.append(int(num % fiBase))    # >(8%2 = 0 / 4%2 = 0 / 2%2 = 0 / 1%2 = 1 )      >(9%4 = 1 / 2%4 = 2)
        num //= fiBase                      # >(n = 4 / 2 / 1)                               >(n = 4 / 0 )
    digits = digits[::-1]                   # >(digits = [0,0,0,1] --> digits = [1,0,0,0])   >([2,1])

    # apply base
    fNum = ""                       
    for x in range(0,len(digits)):  # >(0,4)
        fNum += fiBaseStr[digits[x]]   # >("21")

    if (fiBase == 10):
        return int(fNum)
    else:
        return fNum

#print(b2b(2**32-1,10,16) )