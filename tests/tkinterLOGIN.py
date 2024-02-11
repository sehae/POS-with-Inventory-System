import tkinter as tk
from tkinter import ttk

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Add your authentication logic here
    # For simplicity, let's just print the entered credentials
    print("Username:", username)
    print("Password:", password)

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Login")

    # Create and configure the main frame
    main_frame = ttk.Frame(root, padding=(20, 10))
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Create and place widgets in the main frame
    label_username = ttk.Label(main_frame, text="Username:")
    label_password = ttk.Label(main_frame, text="Password:")
    entry_username = ttk.Entry(main_frame)
    entry_password = ttk.Entry(main_frame, show="*")  # Show asterisks for password input

    button_login = ttk.Button(main_frame, text="Login", command=login)

    # Grid layout for widgets
    label_username.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    entry_username.grid(row=0, column=1, sticky=(tk.E, tk.W), padx=5, pady=5)
    label_password.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    entry_password.grid(row=1, column=1, sticky=(tk.E, tk.W), padx=5, pady=5)
    button_login.grid(row=2, column=0, columnspan=2, pady=10)

    # Configure column weights to make the entry fields expandable
    main_frame.columnconfigure(1, weight=1)

    # Run the main loop
    root.mainloop()
