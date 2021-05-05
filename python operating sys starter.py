import tkinter as tk
from tkinter import messagebox

def Home_screan():
    home = tk.Tk
    home.title("Home Screan ")
    
    

def save(What_to_save):
    return(What_to_save)

def save2(What_to_save2):
    return(What_to_save2)

def save3(What_to_save3):
    return(What_to_save3)


def Check():
    entry1 = save
    entry2 = save2
    entry3 = save3
    if entry1 == "Chinmay M":
         nameTrueOrFalse = True
    else:
     nameTrueOrFalse = False


    if entry2 == "chinmay.malvania@gmail.com":
        emailTrueOrFalse = True
    else:
     emailTrueOrFalse = False


     if entry3 == "111":
         passwordTrueOrFalse = True
     else:
         passwordTrueOrFalse = False


     if emailTrueOrFalse == False or nameTrueOrFalse == False or passwordTrueOrFalse == False or emailTrueOrFalse ==False:
            messagebox.showerror("Error", "Your email, name or password is incorrect")
     #else:
            #Home_screan()

            

def SignIn():
   
    parent = tk.Tk()
    parent.title("Sign in")
    parent.geometry("10000000x10000000")
    name = tk.Label(parent, text = "Name").place(x = 30, y = 50)
  
    email = tk.Label(parent, text = "User ID").place(x = 30, y = 90)

    password =  tk.Label(parent, text = "Password").place(x = 30, y = 130)
    entry1 = tk.Entry(parent).place(x = 85, y = 50)
   
    entry2 = tk.Entry(parent).place(x = 85, y = 90)
    
    entry3 = tk.Entry(parent).place(x = 90, y = 130)
   
    sbmitbtn = tk.Button(parent, text = "Sign in", activebackground = "green", activeforeground = "blue", command = Check).place(x = 120, y = 170)
    save(entry1)
    save2(entry2)
    save3(entry3)
    
    parent.mainloop()






win = tk.Tk()
win.title("Please sign in")
win.geometry("10000000x10000000")

B = tk.Button(win, text = "Sign in",
              bg = "green",
              command = SignIn)
B.place(x = 50,y = 50)
win.mainloop()
