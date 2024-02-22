import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import configparser
import os
import sys

class setupwizard:
    def __init__(self, root):
        self.root = root
        self.root.title("Setup Wizard")
        # Create a frame
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Set up MySQL connection details
        self.mysql_host = tk.StringVar()
        self.mysql_user = tk.StringVar()
        self.mysql_password = tk.StringVar()
        self.mysql_database = tk.StringVar()

        # Create labels and entry widgets
        ttk.Label(self.frame, text="MySQL Host:").grid(column=0, row=0, sticky=tk.W)
        ttk.Entry(self.frame, textvariable=self.mysql_host).grid(column=1, row=0, sticky=(tk.W, tk.E))

        ttk.Label(self.frame, text="MySQL User:").grid(column=0, row=1, sticky=tk.W)
        ttk.Entry(self.frame, textvariable=self.mysql_user).grid(column=1, row=1, sticky=(tk.W, tk.E))

        ttk.Label(self.frame, text="MySQL Password:").grid(column=0, row=2, sticky=tk.W)
        ttk.Entry(self.frame, textvariable=self.mysql_password, show="*").grid(column=1, row=2, sticky=(tk.W, tk.E))

        ttk.Label(self.frame, text="MySQL Database:").grid(column=0, row=3, sticky=tk.W)
        ttk.Entry(self.frame, textvariable=self.mysql_database).grid(column=1, row=3, sticky=(tk.W, tk.E))

        # Create "Save" button
        ttk.Button(self.frame, text="Save", command=self.save_config).grid(column=0, row=4, columnspan=2)

    def save_config(self):
        # Check if mandatory fields are filled
        if not all([self.mysql_host.get(), self.mysql_user.get(), self.mysql_password.get(), self.mysql_database.get()]):
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # Save the configuration to a file
        config = configparser.ConfigParser()
        config['mysql'] = {
            'host': self.mysql_host.get(),
            'user': self.mysql_user.get(),
            'password': self.mysql_password.get(),
            'database': self.mysql_database.get()
        }

        # Get the script directory using the generic approach
        script_directory = get_script_directory()

        # Specify the path for config.ini within the script directory
        config_path = script_directory / 'config.ini'

        # Check if the file exists before writing to it
        if not config_path.is_file():
            with open(config_path, 'w') as configfile:
                config.write(configfile)
            messagebox.showinfo("Success", "Configuration saved successfully.")
        else:
            messagebox.showinfo("Info", "Configuration file already exists.")
        self.root.destroy()

def get_script_directory():
    if getattr(sys, 'frozen', False):
        # Running as frozen executable
        return Path(sys.executable).parent
    else:
        # Running as a regular Python script
        return Path(os.path.dirname(os.path.abspath(__file__)))

def main():
    root = tk.Tk()
    wizard = setupwizard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
