import string
import random

#Function for the Password Gererating
def generate():
    s1= string.ascii_uppercase

    s2= string.ascii_lowercase

    s3=string.digits

    s4=string.punctuation

    #Password Lenght 
    passlen=input("Enter the Password lenght in a digit format (e.g 7 ):  ")

    passlen = int(passlen)
    
    
    s=[]
    s.extend(list(s1))

    s.extend(list(s2))

    s.extend(list(s3))

    s.extend(list(s4))
    #print(s)

    random.shuffle(s)
    #print(s)
    password=("".join(s[0:passlen]))
    print(password)

    
generate()