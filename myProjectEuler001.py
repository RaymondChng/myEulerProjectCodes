# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def ReturnMultiple_of_3_or_5(num):
    if num % 3 == 0 or num % 5 == 0:
        return num
    else:
        return 0

# Process
    
sum = 0
for n in range(1,1000):
    sum = sum + ReturnMultiple_of_3_or_5(n)

# Print Output
    
print(sum)
