import string
import random

def generate():
    s1= string.ascii_uppercase

    s2= string.ascii_lowercase

    s3=string.digits

    s4=string.punctuation

    passlen=input("Enter the Password lenght\n")

    passlen = int(passlen)
    
    
    s=[]
    s.extend(list(s1))

    s.extend(list(s2))

    s.extend(list(s3))

    s.extend(list(s4))
    