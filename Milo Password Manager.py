from tkinter import messagebox
from tkinter import *
import random
import pyperclip3
import json
##############################copy to clipboard###################################


def copy():
    to_copy = password_entry.get()
    pyperclip3.copy(to_copy)
#######################search functionality########################################


def search():
    target = website_entry.get()

    try:
        with open("data.json", mode="r") as datafile:
            data = json.load(datafile)

    except FileNotFoundError:
        messagebox.showwarning(title="No Info Available",
                               message="Please insert some data first")

    else:
        if target in data:
            email_to_get = data[target]["email"]
            password_to_get = data[target]["password"]
            messagebox.showinfo(
                title=f"Info about {target}", message=f"email: {email_to_get}\n password: {password_to_get}")
        else:
            messagebox.showerror(
                "Info not found", message="this website doesn't exist in the database")


########################################save the data################################
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Missing Info",
                             message="Please fill in all the inputs")
    else:
        try:
            with open("data.json", mode="r") as datafile:
                data = json.load(datafile)

        except FileNotFoundError:
            with open("data.json", mode="w") as datafile:
                json.dump(new_data, datafile, indent=4)

        else:
            if website in data and email in data[website]["email"] and password in data[website]["password"]:
                messagebox.showerror(
                    title=f"repeated input", message=f"{website} already exists with the same email and password entered")
            else:
                data.update(new_data)
                with open("data.json", mode="w") as datafile:
                    json.dump(data, datafile, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)


############################add default email##############################
def default_email():
    email_entry.delete(0, END)
    email_entry.insert(0, "miladbannourah@outlook.com")


################################Random password Generator###################
ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
             'y', 'z', 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SYMBOLS = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '/']


def generate_pass():
    password_entry.delete(0, END)

    semi_pass = []

    for number in range(5):
        number = random.choice(NUMBERS)
        semi_pass.append(number)

    for letter in range(6):
        letter = random.choice(ALPHABETS)
        semi_pass.append(letter)

    for symbol in range(4):
        symbol = random.choice(SYMBOLS)
        semi_pass.append(symbol)

    random.shuffle(semi_pass)

    final_pass = ""

    for element in semi_pass:
        final_pass += element

    password_entry.insert(0, final_pass)
    pyperclip3.copy(final_pass)


#############################User Interface######################################
window = Tk()
window.title("Milo Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(height=200, width=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website", font=("Arial", 15, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email", font=("Arial", 15, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password", font=("Arial", 15, "bold"))
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)


# buttons
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

deafault_email_button = Button(text="Default", width=15, command=default_email)
deafault_email_button.grid(row=2, column=2)

generate_pass_button = Button(
    text="Generate Password", width=15, command=generate_pass)
generate_pass_button.grid(row=3, column=2)

copy_pass_button = Button(
    text="Copy Password to clipboard", width=46, command=copy)
copy_pass_button.grid(row=4, column=1, columnspan=2)

add_button = Button(text="ADD Password to DataBase",
                    width=46, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
