import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    # adding all lists
    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    # converting list to string
    password = "".join(password_list)

    # populating in the password entry box
    input_password.insert(0, password)
    pyperclip.copy(password)  # passwrd gets copied to clipboard. can paste anywhere


# ---------------------------- SAVE PASSWORD ------------------------------- #
# function for ADD button
def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    # asking if the user wants to save info
    # is_ok results in boolean
    # making a file
    if len(website) == 0 or len(email) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty")
    else:
        # is_ok = messagebox.askokcancel(title=website,
        #                                message=f"These are the details entered:\nEmail: {email}\nPassword: {password} \n is it ok to save")
        #
        # if is_ok:
        try:
            with open("data.json", "r") as file:  # mode 'a' so it keeps the old data
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                # updating old data with new data
                data.update(new_data)
                # saving updated data
                json.dump(data, file, indent=4)
                # file.write(f"{website} | {password} | {email}\n")
                # keeps the email and clears website and password
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)


def find_password():
    website = input_website.get()
    #try if the file exists
    try:
        with open("data.json", "r") as file:
            data_loaded = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data_loaded:
            messagebox.showinfo(title=website, message=f"Email: {data_loaded[website]['email']}\nPassword: {data_loaded[website]['password']}")
        else:
            messagebox.showinfo(message=f"No details for the {website} exists")

# ---------------------------- UI SETUP ------------------------------- #

# window created
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create canvas
canvas = Canvas(height=200, width=200)

# add image
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website", font=("Arial", 10))
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username", font=("Arial", 10))
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password", font=("Arial", 10))
password_label.grid(row=3, column=0)

# Entry
input_website = Entry(width=32)
input_website.grid(row=1, column=1)
input_website.focus()

input_email = Entry(width=50)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "bonny99@gmail.com")

input_password = Entry(width=32)
input_password.grid(row=3, column=1)

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
