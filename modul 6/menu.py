import tkinter as tk
from tkinter import messagebox

def show_profile():
    # Tampilkan konten profile
    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")
    profile_label = tk.Label(profile_window, text="Nama: Mitsuha\nAvatar: [Gambar Avatar]")
    profile_label.pack(padx=20, pady=20)

root = tk.Tk()
root.title("Menu Example")

# Fungsi untuk menampilkan pesan dialog

# Membuat menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Membuat menu File
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=menu_file)
menu_file.add_command(label="New")
menu_file.add_command(label="Open")
menu_file.add_command(label="Save")
menu_file.add_command(label="Close")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

# Membuat menu Home
menu_home = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Home", menu=menu_home)
menu_home.add_command(label="Home")
menu_home.add_command(label="Profile", command=show_profile)
menu_home.add_command(label="Settings")

# Membuat menu Edit
menu_edit = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=menu_edit)
menu_edit.add_command(label="Cut")
menu_edit.add_command(label="Copy")
menu_edit.add_command(label="Paste")

# Membuat menu About Me
menu_about = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About Me", menu=menu_about)
menu_about.add_command(label="About Me")
menu_about.add_command(label="Contact")
menu_about.add_command(label="Help")

root.mainloop()
