def getFlag(num):
    res= False
    for i in range(2,num):
        if num%i==0:
            res= True
            break
    return (not res)


def primes():
    n=2
    while True:
        flag = False
        flag=getFlag(n)
        if flag==True:
            yield n
        n +=1