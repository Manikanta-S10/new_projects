from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Enter each and every field")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"You entered detailes are\n Website:{website}\n Password:{password}\n Email:{email} is that okay to save")

        if is_ok:
            with open('newfile.txt','a') as file:
                file.write(f"{website} |{email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)      


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password genarator')
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

#labels
website_label = Label(text='Website:')
website_label.grid(column=0,row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0,row=2)
password_label = Label(text='Password:')
password_label.grid(column=0,row=3)

#entry
website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(0,'mani@gmai.com')
email_entry.grid(column=1,row=2,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

#buttons
generate_button = Button(text='Generate Password')
generate_button.grid(column=2,row=3)

add_button = Button(text='Add',width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()