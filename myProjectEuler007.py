"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10001st prime number?
"""
num = 10001

def getSieve(n):
    mylist = [True] * n
    mylist[0] = False
    mylist[1] = False
    for i in range(2, n):
        if mylist[i]:
            for j in range(i*i, n, i):
                mylist[j] = False
    return mylist

def getListOfPrimes(n):
    myPrimeList = []
    mylist = getSieve(n*n)
    number = 2
    while len(myPrimeList) < n:
        if mylist[number]:
            myPrimeList.append(number)
        number = number + 1
    return myPrimeList

finalList = getListOfPrimes(num)
print(finalList[-1])
