import tkinter as tk
#widget ComboBox ada di modul ttk dalam tkinter
from tkinter import ttk

from functools import partial

def fungsiTampil(labelHasil, namaCbBox):
    n1 = namaCbBox.get()
    hasil = n1
    labelHasil.config(text=hasil)
    return

root = tk.Tk()
root.title('ComboBox')
root.geometry('300x200+500+100')

#font digunakan oleh semua widget
root.option_add('*font', ('Verdana', 10, 'normal'))

#font digunakan oleh semua widget label
root.option_add('*Label.font', ('Verdana', 10, 'bold'))

labelPilihOperator = tk.Label(root, text="Pilih Operator")
labelPilihOperator.grid(row=0, column=0, sticky="w", padx=(5,0), pady=(5,5))

namaCbBox = tk.StringVar()
comboPilihOperator = ttk.Combobox(root, values=["+","-","*","/"], textvariable=namaCbBox)
comboPilihOperator.grid(row=1, column=0, padx=(5,0), pady=(0,5))

#0 artinya menampilkan value pertamacomboBox yaitu simbol (+)
comboPilihOperator.current(0)

labelHasil = tk.Label(root)
labelHasil.grid(row=3, column=0)

tampil = partial(fungsiTampil, labelHasil, namaCbBox)
tombolTampil = tk.Button(root, text="Tampil", command=tampil)
tombolTampil.grid(row=2, column=0, sticky="WE", padx=(5,0))
tombolTampil.configure(bg="#000", fg="#FFF")
root.mainloop()