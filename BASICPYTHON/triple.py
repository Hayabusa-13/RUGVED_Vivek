'''
Define a function named “triple_and” that takes three parameters and returns True 
only if they are all True and False otherwise
'''
def triple_and(a, b, c):
    return a and b and c
x = 4>5
y= 1==0
z = 21>20
print(triple_and(x,y,z))