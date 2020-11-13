# --- Directions
# Print out the n-th entry in the fibonacci series.
# The fibonacci series is an ordering of numbers where
# each number is the sum of the preceeding two.
# For example, the sequence
#  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# forms the first ten entries of the fibonacci series.
# Example:
#   fib(4) === 3
cache = {}

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    

def fib(n):
    result = [0,1]
    for i in range(2,n+1):
        a = result[i-1]
        b = result[i-2]
        result.append(a+b)
    return result[n]


def fib_rec(n):
    if n<=1: return n
    return fib_rec(n-1) + fib_rec(n-2)

def fib_faster(n):
    if n<=1: return n
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

def main():
    print("Fibonacci Series")
    number = int(input("Input a  number:"))
    fib = memoize(fib_rec)
    print_em = fib(number)
    
    print(print_em) 
     
main()