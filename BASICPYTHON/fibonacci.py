def fib(n):
   if n==0:
      return 0
   elif n==1:
      return 1
   else:
      return fib(n-1)+fib(n-2)

num = int(input("Enter the limit of the sequence :"))
print(fib(num))
for i in range(num):
   print(fib(i), end=",")