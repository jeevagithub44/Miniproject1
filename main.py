import os
import sys
from tkinter import *
import tkinter as tk
from pathlib import Path
from crud import crud
from export import ImportExportData
from win32com.client import Dispatch
import ctypes

class myapp:
    def create_desktop_shortcut(self):
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        shortcut_path = os.path.join(desktop_path, 'AlumniManagement.lnk')

        if not os.path.isfile(shortcut_path):
            python_exe = sys.executable
            script_path = os.path.abspath(__file__)

            # Get the path to the Python executable
            python_exe = sys.executable

            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = python_exe
            shortcut.Arguments = f'"{script_path}"'
            shortcut.IconLocation = python_exe  # Optional: Set the icon location

            # Set the working directory to the project folder
            shortcut.WorkingDirectory = os.path.dirname(script_path)

            shortcut.save()
            ctypes.windll.user32.MessageBoxW(0, "Desktop shortcut created.", "Success", 1)

    def __init__(self, root):
        self.root = root
        self.create_desktop_shortcut()

        # Calculate the desired percentage (e.g., 80% of screen width and 60% of screen height)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        frame_width = int(screen_width * 0.2)
        frame_height = int(screen_height * 0.80)

        # Sidebar
        self.sidebar = tk.Frame(root, bg='#1d4989')
        self.sidebar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Mainframe for content
        self.mainframe = tk.Frame(root, bg='#73d460')
        self.mainframe.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        
        # Creating frames for mainframe
        self.frame1 = tk.Frame(self.mainframe, bg="#ff5733")
        ''' self.frame1.pack(fill=tk.BOTH, expand=True)'''

        self.frame2 = tk.Frame(self.mainframe, bg="#fcb603")
        '''self.frame2.pack(fill=tk.BOTH, expand=True)'''

        self.frame3 = tk.Frame(self.mainframe, bg="#73d460")
        '''self.frame3.pack(fill=tk.BOTH, expand=True)'''

        # Creating buttons
        b1 = tk.Button(self.sidebar, text="CRUD", background="#34eb98", fg="white", command=self.showframe1)
        b1.pack(side=TOP, pady=10, fill=BOTH)

        b2 = tk.Button(self.sidebar, text="DASHBOARD", background="#34eb98", fg="white", command=self.showframe2)
        b2.pack(side=TOP, pady=10, fill=BOTH)

        b3 = tk.Button(self.sidebar, text="EXPORT", background="#34eb98", fg="white", command=self.showframe3)
        b3.pack(side=TOP, pady=10, fill=BOTH)

        # Passing frame into child class
        self.child = crud(self.frame1)
        self.frame1.pack(fill=tk.BOTH, expand=True)

        child3 = ImportExportData(self.frame3,config_file='config.ini')
        child3.createbutton(self.frame3)

    def showframe1(self):
        self.frame1.pack(fill=tk.BOTH, expand=True)
        self.frame2.pack_forget()
        self.frame3.pack_forget()

    def showframe2(self):
        self.frame1.pack_forget()
        self.frame2.pack(fill=tk.BOTH, expand=True)
        self.frame3.pack_forget()

    def showframe3(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack(fill=tk.BOTH, expand=True)

        print("frame called")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('1920x1080')
    root.title('ALUMNI MANAGEMENT')
    app = myapp(root)
    root.mainloop()
