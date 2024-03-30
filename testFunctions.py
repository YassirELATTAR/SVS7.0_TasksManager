import tkinter as tk
import customtkinter as ctk

def submit_form():
    # Retrieve input values from the form
    name = name_entry.get()
    email = email_entry.get()

    # Display a message
    result_label.config(text=f"Hello, {name}! Your email is {email}.")

# Create the main window
root = tk.Tk()
root.title("CustomTkinter Form")

# Create form elements
name_label = ctk.Label(root, text="Name:")
name_entry = ctk.Entry(root)
email_label = ctk.Label(root, text="Email:")
email_entry = ctk.Entry(root)
submit_button = ctk.Button(root, text="Submit", command=submit_form)
result_label = ctk.Label(root, text="")

# Arrange form elements using grid layout
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry.grid(row=0, column=1, padx=10, pady=5)
email_label.grid(row=1, column=0, padx=10, pady=5)
email_entry.grid(row=1, column=1, padx=10, pady=5)
submit_button.grid(row=2, columnspan=2, padx=10, pady=10)
result_label.grid(row=3, columnspan=2, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
