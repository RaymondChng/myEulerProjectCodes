"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

num = 2000000

def getSieve(n):
    mylist = [True] * n
    mylist[0] = False
    mylist[1] = False
    for i in range(2, n):
        if mylist[i]:
            for j in range(i*i, n, i):
                mylist[j] = False
    return mylist

def getSumOfPrimes(n):
    sumOfPrimes = 0
    mylist = getSieve(n)
    for i in range(2, n):
        if mylist[i]:
            sumOfPrimes = sumOfPrimes + i
    return sumOfPrimes

print(getSumOfPrimes(num))


