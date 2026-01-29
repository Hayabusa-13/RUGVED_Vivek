
def caeser(string,num):
    l = "abcdefghijklmnopqrstuvwxyz"
    u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = ""
    for x in string:
        if x in l:
            i =l.index(x)
            final += l[(i+ num) % 26]
        elif x in u:
            i = u.index(x)
            final += u[(i+num) % 26]
        else:
            final += x
    print("Ciphered word is : " , final)        
string = input("Please enter the string: \n")
num = int(input("Enter the number of shifts for Caeser's Ciphers:\n"))
caeser(string,num)