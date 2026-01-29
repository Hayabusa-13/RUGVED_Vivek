def selesort(x):
    n = len(x)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if x[j] < x[min]:
                min = j
        temp   = x[i]
        x[i]   = x[min]
        x[min] = temp
    new = ','.join(x)        
    return new      
string = input("Please enter the string: \n")
newstr = list(string)
print(selesort(newstr))
#Do it using bubble sort recursion