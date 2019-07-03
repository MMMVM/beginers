s=input()
if(s>="a" and s<="z"):
    list=["a","e","i","o","u"]
    if s in list:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
