from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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

    if len(website_data)==0 or len(email_data)==0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \nEmail:{email_data} "
                                                  f"\nPassword:{password_data}\nIs it ok to save?")
        if is_ok:
            with open("passwordFile.txt", "a") as f:
                f.write(f"{website_data} | {email_data} | {password_data}")
                f.write("\n")
                website_input.delete(0,END)
                email_name_input.delete(0, END)
                password_input.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# TODO 1: Add Image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1,row=0)

# TODO 2: Add Text and set grid
website_text = Label(text="Website: ")
website_text.grid(column=0, row=1)

email_name = Label(text="Email/Username: ")
email_name.grid(column=0, row=2)

password_text = Label(text="Password: ")
password_text.grid(column=0, row=3)



# TODO 3: Add Input Box
website_input = Entry(width=43)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()


email_name_input = Entry(width=43)
email_name_input.grid(column=1, row=2, columnspan=2)
email_name_input.insert(0, "boon123@gmail.com")

password_input = Entry(width=25)
password_input.grid(column=1, row=3)

# TODO 4: Add Button
generate_pass_button = Button(text="Generate Password", width=14, command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()