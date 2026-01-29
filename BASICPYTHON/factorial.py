
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter the number :\n"))   
print(f"The factorial of {num} = " , factorial(num))
# check it iteratively 