# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143

def getLargestFactor(n):
    while True:
        p = getNextSmallestFactor(n) 
        if p < n:
            n = n // p      # Divides by the current smallest prime factor
        else:
            return n        # When the current smallest prime factor is the only prime factor remaining

def getNextSmallestFactor(n):
    for i in range(2, n):   # Begin with the smallest prime factor which is 2
        if n % i == 0:
            return i
    return n                # when n is a prime number

print(getLargestFactor(num))




