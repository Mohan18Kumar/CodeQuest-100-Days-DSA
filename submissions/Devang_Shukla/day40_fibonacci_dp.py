def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
def main():
    n = int(input("Enter a number (n): "))
    print("Fibonacci number:", fibonacci(n))
if __name__ == "_main_":
    main()