num= input("Enter the number: ")

n = len(num)
    
if n < 3:
        print("The no.of digits should be atlest 3 for it to be a hill number ,\n So Rerun the program ")

else:
    i = 0
    while i < n - 1 and num[i] < num[i+1]:
            i += 1
    if i == 0 :
            print("The number is  purely decresing so no it isnt a hill number")
    elif i == n-1:
          print("purely Incresing")        
    else:
        while i < n - 1 and num[i] > num[i+1]:
                i += 1

        if i <= n:
            print("Yesss the number is a hill number")
        else :
            print("Sry the number isnt a hill number")    