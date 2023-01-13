# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def reverseStr(n):
        return n[::-1]          # Returns the string in reverse order

def getLargestPalindrome():
        pal = 0
        
        for x in range(100, 1000):
                for y in range(100, 1000):
                        new_pal = x * y
                        p1 = str(new_pal)                               # Converts to a string
                        p2 = reverseStr(p1)
                        if p1 == p2 and pal < new_pal : 
                                pal = new_pal                             # Updates variable with larger palindrone

        return pal

print(getLargestPalindrome())
