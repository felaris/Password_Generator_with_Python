import string
import random
import tkinter as tk

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
    output=open("Passwords.txt" ,"a")

    #This writes outputs on a new line
    output.write( "Password : "+ password + "\n")
    output.close()


    #def dispass():
        #print(output)
        #output.close()


#generate()

root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
canvas1=tk.Canvas(root, height=50)
canvas1.pack()


#Screenshot Button
button=tk.Button(
    frame,
    text = "Generate Password" , 
    command=generate)




#Quit Button
button.pack(side=tk.LEFT)
close=tk.Button(
    frame,
    text="QUIT" ,
    command=quit)
close.pack(side=tk.LEFT)


root.mainloop()