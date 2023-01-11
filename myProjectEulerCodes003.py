# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143

def ReturnLargestFactor(n):
    while True:
        p = ReturnNextSmallestFactor(n) 
        if p < n:
            n = n // p  # Removes the current smallest prime factor
        else:
            return n    

def ReturnNextSmallestFactor(n):
    for i in range(2, n):   # Begin with the smallest prime factor which is 2
        if n % i == 0:
            return i
    return n                # when n is a prime number

print(ReturnLargestFactor(num))




