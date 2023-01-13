# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num = 20

def getLCM(x, y):
        if x > y:
                x, y = y, x                  # Let y be the larger factor
        lcm = y
        while(True):
                if lcm % x == 0 and lcm % y ==0:
                        return lcm
                lcm = lcm + 1           # Increment lcm until it is divisible by both x and y

def getSmallestPositiveNumber(x):
        lcm = 1
        for i in range(1, x):
                lcm = getLCM(i, lcm)
        return lcm

print(getSmallestPositiveNumber(num))
