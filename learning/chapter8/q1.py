# Write a recursive function to calculate the sum of first n natural numbers.
def firstN(n):
    return firstNHelper(n,0)

def firstNHelper(n,sum):
    if(n==0):
        return 0
    sum+=n+firstNHelper(n-1,sum)
    return sum

print(firstN(10))