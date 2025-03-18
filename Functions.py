def compare_numbers():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))

    if a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{b} is greater than {a}"
    


def factorial(n):

    # Base condition

    if n==0 |  n == 1 :
        return 1
    else:
   
        # find the factorial of n! = n * (n-1)  
        factorial_result= n * factorial(n-1)
        return factorial_result
    


# compare_numbers()
number=int(input("Enter a number:"))
n_factorial=factorial(number)
print(f"The Factorial of {number} is {n_factorial}")
