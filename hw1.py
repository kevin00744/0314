# Define Fibonacci(n) to print the first n Fibonacci
# numbers as follows.
# • 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …
# • Hint: Using recursive equation: F(n)=F(n-1)+F(n-2)
# with initial conditions F(1)=1 and F(2)=1.
def Fibonacci(n=1):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
def print_Fibonacci(n=1):
    n = int(input('Input how many number you want to see\n>'))
    for i in range (1,n):
        print ('%s,' % Fibonacci(i),  sep = "", end = "")
    print (Fibonacci(n))
print_Fibonacci()

