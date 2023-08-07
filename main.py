from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
     website = website_entry.get()
     email = email_entry.get()
     password = password_entry.get()

     if len(website) == 0 or len(password) == 0:
         messagebox.showinfo(title="Oops",message="Please make sure you do not leave any field empty!")
     else:
         is_ok= messagebox.askokcancel(title=website,message=f"these are the details, entered:\nEmail: {email}"
                                                     f"\nPassword: {password} \nis it ok to save?")

         if is_ok:
              with open("data.txt", "a") as data_file:
                  data_file.write(f"{website} / {email} / {password}\n")
                  website_entry.delete(0, END)
                  password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(height=200,width=200)
my_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=my_image)
canvas.grid(column=1,row=0)

#Website label and entry:
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2)

#Email and username label and entry:
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
email_entry = Entry(width=35)
email_entry.insert(0,"anthonyzambrano0904@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)

#Password Label and entry:
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

#Generate password Button:
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

#Add button:
add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()
