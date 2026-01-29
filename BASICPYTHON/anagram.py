s1 = input("String 1 :")
s2 = input("String 2 :")
t1 = ''.join(sorted(s1))
t2 = ''.join(sorted(s2))
if len(t1)!= len(t2):
    print("NOT ANAGRAMS!!!")
elif t1 == t2 :
    print("YES THEY ARE ANAGRAMS!!!")
else:
    print("NOT ANAGRAMS!!!")   
