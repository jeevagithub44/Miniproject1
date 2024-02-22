import mysql.connector
from configparser import ConfigParser
from pathlib import Path
import tkinter as tk
from setupwizard import setupwizard

class database:
    def __init__(self, config_file='config.ini'):
        # Check if the INI file exists
        config_path = Path(config_file)
        if not config_path.is_file():
            print(f"Config file '{config_file}' not found. Running setup wizard...")
            self.run_setup_wizard()
        
        # Read configuration from INI file
        config = ConfigParser()
        config.read(config_file)

        # Storing connection values
        self.db_config = {
            'host': config.get('mysql', 'host'),
            'user': config.get('mysql', 'user'),
            'password': config.get('mysql', 'password'),
            'database': config.get('mysql', 'database')
        }

        # Create connection
        self.connection = mysql.connector.connect(**self.db_config)
        self.cur = self.connection.cursor()

        # Create employees table if not exists
        sql = """CREATE TABLE IF NOT EXISTS employees(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name text,
            age text,
            gender text,
            email text,
            contact text,
            address text
        )"""
        self.cur.execute(sql)
        self.connection.commit()
        print("Connection established successfully")
    

    def run_setup_wizard(self):
         # Create a new Tk instance
        root = tk.Tk()

    # Call setup wizard to create the INI file
        wizard = setupwizard(root)
        print("Setup wizard completed.")

    # Run the main loop to keep the window open until it's closed
        root.mainloop()


    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, age, gender, email, contact, address):
        # id will be generated automatically (primary)
        sql = "INSERT INTO employees (name, age, gender, email, contact, address) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, age, gender, email, contact, address)
        self.cur.execute(sql, values)
        self.connection.commit()

    def update(self, name, age, gender, email, contact, address, idvar):
        id_value = int(idvar.get())
        sql = "UPDATE employees SET name=%s, age=%s, gender=%s, email=%s, contact=%s, address=%s WHERE id=%s"
        values = (name, age, gender, email, contact, address, id_value)
        self.cur.execute(sql, values)
        self.connection.commit()

    def delete(self, idvar):
        id_value = int(idvar.get())
        sql = "DELETE FROM employees WHERE id=%s"
        values = (id_value,)
        self.cur.execute(sql, values)
        self.connection.commit()

# If this script is run directly, create an instance of the database class
if __name__ == "__main__":
    db = database()
