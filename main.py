from tkinter import Tk, Label, Entry, Button
from Models.phone_book import PhoneBook

phone_book = PhoneBook()

phone_book.create_contact("Mobina", "Bayati", "09384864724")
phone_book.create_contact("Dina", "Bayati", "09108352841")
phone_book.create_contact("Azam", "Rezaie", "09126843160")
phone_book.create_contact("Mojtaba", "Bayati", "09103229692")
phone_book.create_contact("Kimia", "Nemati", "09364578884")

window = Tk()
window.title("Phone Book Application")


def show_contact_form(id=None, firstname="", lastname="", phone=""):
    contact_form = Tk()
    if not id:
        contact_form.title = "create contact form"
    else:
        contact_form.title = "update contact form"

    firstname_label = Label(contact_form, text="First Name")
    firstname_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

    firstname_entry = Entry(contact_form, width=30)
    firstname_entry.grid(row=0, column=1, pady=10, padx=(0, 20), sticky="w")
    firstname_entry.insert(0, firstname)

    lastname_label = Label(contact_form, text="Last Name")
    lastname_label.grid(row=1, column=0, pady=10, padx=10, sticky="e")

    lastname_entry = Entry(contact_form, width=30)
    lastname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="w")
    lastname_entry.insert(0, lastname)

    phone_number_label = Label(contact_form, text="Phone Number")
    phone_number_label.grid(row=2, column=0, pady=10, padx=10, sticky="e")

    phone_number_entry = Entry(contact_form, width=30)
    phone_number_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="w")
    phone_number_entry.insert(0, phone)

    def sumbit():
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        phone = phone_number_entry.get()

        if not id:
            phone_book.create_contact(firstname, lastname, phone)
        else:
            update_contact = phone_book.get_contact(id)
            update_contact.update(firstname, lastname, phone)
            phone_book.show_contact_list = phone_book.contact_list.copy()

        create_table_body()

        contact_form.destroy()

    submit_button = Button(contact_form, text="Submit", command=sumbit)
    submit_button.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="w")

    contact_form.mainloop()


new_contact_button = Button(window, text="New Contact", command=show_contact_form)
new_contact_button.grid(row=0, column=1, pady=10, padx=0, sticky="w")

search_entry = Entry(window, width=50)
search_entry.grid(row=0, column=2, pady=10, padx=0, sticky="e")


def search():
    term = search_entry.get()

    phone_book.search(term)

    create_table_body()


search_button = Button(window, text="search",command=search)
search_button.grid(row=0, column=3, pady=10, padx=0, sticky="w")


def create_table_header():
    row_label = Label(window, text="NO")
    row_label.grid(row=1, column=0, pady=0, padx=0, sticky="ew")

    firstname_label = Label(window, text="FIRST NAME")
    firstname_label.grid(row=1, column=1, pady=0, padx=0, sticky="ew")

    lastname_label = Label(window, text="LAST NAME")
    lastname_label.grid(row=1, column=2, pady=0, padx=0, sticky="ew")

    phone_label = Label(window, text="PHONE NUMBER")
    phone_label.grid(row=1, column=3, pady=0, padx=0, sticky="ew")


create_table_header()

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

entry_list = []


def create_table_body():
    for entry in entry_list:
        entry.destroy()

    entry_list.clear()
    # something like updating

    row_number = 1
    for contact in phone_book.show_contact_list:
        row_entry = Entry(window, width=5)
        row_entry.insert(0, str(row_number))
        row_entry.config(state="readonly")
        row_entry.grid(row=row_number + 1, column=0)
        entry_list.append(row_entry)

        firstname_entry = Entry(window, width=30)
        firstname_entry.insert(0, contact.first_name)
        firstname_entry.config(state="readonly")
        firstname_entry.grid(row=row_number + 1, column=1)
        entry_list.append(firstname_entry)

        lastname_entry = Entry(window, width=30)
        lastname_entry.insert(0, contact.last_name)
        lastname_entry.config(state="readonly")
        lastname_entry.grid(row=row_number + 1, column=2)
        entry_list.append(lastname_entry)

        phone_entry = Entry(window, width=30)
        phone_entry.insert(0, contact.phone_number)
        phone_entry.config(state="readonly")
        phone_entry.grid(row=row_number + 1, column=3)
        entry_list.append(phone_entry)

        delete_button = Button(window, text="Delete", command=lambda contact_id=contact.id: delete_contact(contact_id))
        delete_button.grid(row=row_number + 1, column=4)
        entry_list.append(delete_button)

        update_button = Button(window, text="Update", command=lambda id=contact.id,
                                                                     firstname=contact.first_name,
                                                                     lastname=contact.last_name,
                                                                     phone=contact.phone_number: show_contact_form(id,
                                                                                                                   firstname,
                                                                                                                   lastname,
                                                                                                                   phone))
        update_button.grid(row=row_number + 1, column=5)
        entry_list.append(update_button)

        row_number += 1


def delete_contact(contact_id):
    phone_book.delete_contact(contact_id)
    create_table_body()


create_table_body()

window.mainloop()
