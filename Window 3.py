import tkinter as tk 
from tkinter import ttk 
import subprocess 
import sys 
import os 
# Helper function to open another Python window
def open_window(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    subprocess.Popen([sys.executable, script_path])
    root.destroy()

# Main window
root = tk.Tk()
root.title("Main Menu")
root.geometry("960x540")

ttk.Label(root, text="Main Menu", font=("Arial", 40)).pack(pady=20)

# Button 1 → Opens Name Game
name = ttk.Button(root, text="Naming Game", command=lambda: open_window("Window 2.py"), )
name.pack(side= tk.LEFT, padx=50, pady=10)
name.configure(width=50)
# Button 2 → Opens Emotion Game
call = ttk.Button(root, text="Calling Game", command=lambda: open_window("Window.py"), width=50)
call.pack(side= tk.RIGHT, padx=50, pady=10)

root.mainloop()