import tkinter as tk
import random
import string

def generate_password(length, strength):
    characters = string.ascii_lowercase + string.digits
    if strength == 'moderate':
        characters += string.punctuation
    elif strength == 'strong':
        characters += string.ascii_uppercase + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    length = int(length_entry.get())
    strength = strength_var.get()
    password = generate_password(length, strength)
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
length_label = tk.Label(root, text="Enter the desired length of the password:")
length_entry = tk.Entry(root)
length_entry.insert(0, "8")  # default length
strength_label = tk.Label(root, text="Select password strength:")
strength_var = tk.StringVar(root)
strength_var.set("weak")  # default strength
strength_option_menu = tk.OptionMenu(root, strength_var, "weak", "moderate", "strong")
generate_button = tk.Button(root, text="Generate Password", command=generate)
result_label = tk.Label(root, text="")

# Layout widgets
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
length_entry.grid(row=0, column=1, padx=10, pady=5)
strength_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
strength_option_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()
