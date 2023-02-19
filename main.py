from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

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

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    # copy the text to clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website_data = website_input.get()
    email_data = email_name_input.get()
    password_data = password_input.get()

    # TODO 5: create json object
    new_data = {
        website_data:{
            "email": email_data,
            "password": password_data

        }
    }

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        # # TODO 6: save data to json file
        # with open("data.json", "a") as file:
        #     # write data to json file
        #     json.dump(new_data, file, indent=4)
        #     website_input.delete(0,END)
        #     email_name_input.delete(0, END)
        #     password_input.delete(0,END)

        # TODO 7: Update json data
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                # write data to json file
                json.dump(new_data, file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            email_name_input.delete(0, END)
            password_input.delete(0,END)

#----------------------------- Retrieve Data ---------------------------#
def retrive_data():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data_full = json.load(data_file)
            print(data_full)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data_full:
            email = data_full[website]["email"]
            password = data_full[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Your Email: {email}\nYour Password: {password}")

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# TODO 1: Add Image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# TODO 2: Add Text and set grid
website_text = Label(text="Website: ")
website_text.grid(column=0, row=1)

email_name = Label(text="Email/Username: ")
email_name.grid(column=0, row=2)

password_text = Label(text="Password: ")
password_text.grid(column=0, row=3)



# TODO 3: Add Input Box
website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()


email_name_input = Entry(width=50)
email_name_input.grid(column=1, row=2, columnspan=3)
email_name_input.insert(0, "boon123@gmail.com")

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

# TODO 4: Add Button
generate_pass_button = Button(text="Generate Password", width=14, command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=retrive_data)
search_button.grid(column=2,row=1)




window.mainloop()