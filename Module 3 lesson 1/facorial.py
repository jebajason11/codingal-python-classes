def factorial(x):
    """this is a recursive function to find the factorial of an integer"""

    if x==0 or x==1:
        return 1

    else:
        return x*factorial(x-1)



print(factorial.__doc__)
print("the facorial of 0:",factorial(0))
print("the facorial of 1:",factorial(1))
print("the facorial of 2:",factorial(2))
print("the facorial of 5:",factorial(5))
print("the facorial of 10:",factorial(10))