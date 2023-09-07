import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Please enter both name and phone number.")
    else:
        contact = {"Name": name, "Phone": phone}
        contacts.append(contact)
        update_contact_list()
        clear_entries()

def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        for contact in contacts:
            if contact["Name"] == selected_contact:
                contacts.remove(contact)
                update_contact_list()
                break

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, contact["Name"])

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def show_contact_info():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        for contact in contacts:
            if contact["Name"] == selected_contact:
                messagebox.showinfo("Contact Info", f"Name: {contact['Name']}\nPhone: {contact['Phone']}")
                break

root = tk.Tk()
root.title("Contact Book")

name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()

phone_entry = tk.Entry(root)
phone_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=5)

contact_listbox = tk.Listbox(root)
contact_listbox.pack(pady=5)

show_button = tk.Button(root, text="Show Contact Info", command=show_contact_info)
show_button.pack(pady=5)

root.mainloop()