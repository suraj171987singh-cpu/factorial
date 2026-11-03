def factorial(x):
    '''This is a recursive function to calculate the factorial of a number'''
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)

x = int(input("Enter a number to calculate its factorial: "))
print(factorial.__doc__)
print(f"The factorial of {x} is {factorial(x)}")