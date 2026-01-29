string = input("Please enter the string: \n")
count={}

temp=0
newstr = sorted(string)
newstr = ''.join(newstr)#join command joins the string here
for x in string:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
print(newstr)
print("Character count:")
for x in count:
    print(x, "=", count[x])
