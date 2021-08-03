from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Angela Style
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # Dara Style
    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)
    # password_list = []
    #
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    #
    # random.shuffle(password_list)
    #
    # password = ""
    # for char in password_list:
    #     password += char

    print(password)
    pyperclip.copy(password)
    password_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print("Adding")
    web = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    print(web)
    print(email)
    print(password)

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=web,
                                       message=f"These are the detail entered: \nEmail: {email} \nPassword: {password} "
                                               f"\nIs it ok to save?")

        if is_ok:
            f = open("data.txt", "a")
            f.write(f" {web} | {email} | {password}\n")
            f.close()
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)

            # Angela Style
            # with open("data.txt", "a") as data_file:
            #     data_file.write(f"{web} | {email} {password}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=51)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_username_entry = Entry(width=51)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(END, "lyvireakdara007@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
