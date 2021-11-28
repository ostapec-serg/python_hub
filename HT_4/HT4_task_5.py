# 5. Write a function <fibonacci> that takes one argument
# and outputs all Fibonacci numbers not exceeding it
def fibo(n):
    fibo1 = fibo2 = 1

    while fibo2 < n:
        print(fibo2, end=' ')
        fibo1, fibo2 = fibo2, fibo1 + fibo2

fibo(int(input("Enter the end of the Fibonacci range: \n")))
