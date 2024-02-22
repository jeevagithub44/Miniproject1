import os
from cx_Freeze import setup, Executable

# Determine the base parameter based on the operating system
if os.name == "nt":  # For Windows
    base = "Win32GUI"
else:
    base = None

# Setup configuration
setup(
    name="EMP-MANAGEMENT",  # Replace with your application name
    version="1.0",  # Replace with your application version
    description="EMPLOYEE MANAGEMENT Application",  # Replace with your application description
    options={"build_exe": {"packages": ["tkinter", "configparser", "mysql.connector"]}},
    executables=[Executable("main.py")]
)
