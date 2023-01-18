"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

num = 10001

def isPrime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True
        
def getListOfPrimes(n):
    mylist = []
    number = 2
    while len(mylist) < n:
        if isPrime(number):
            mylist.append(number)
        number = number + 1
    return mylist

finalList = getListOfPrimes(num)
print(finalList[-1])
