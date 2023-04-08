import tkinter as tk
from functools import partial

def pertambahan(labelHasil, bil1, bil2, inputHasil):
    b1 = int(bil1.get())
    b2 = int(bil2.get())
    hasil = b1 + b2
    inputHasil.delete(0, tk.END)
    inputHasil.insert(0, hasil)
    return

def pengurangan(labelHasil, bil1, bil2, inputHasil):
    b1 = int(bil1.get())
    b2 = int(bil2.get())
    hasil = b1 - b2
    inputHasil.delete(0, tk.END)
    inputHasil.insert(0, hasil)

def pembagian(labelHasil, bil1, bil2, inputHasil):
    b1 = int(bil1.get())
    b2 = int(bil2.get())
    hasil = b1 / b2
    inputHasil.delete(0, tk.END)
    inputHasil.insert(0, hasil)

def perkalian(labelHasil, bil1, bil2, inputHasil):
    b1 = int(bil1.get())
    b2 = int(bil2.get())
    hasil = b1 * b2
    inputHasil.delete(0, tk.END)
    inputHasil.insert(0, hasil)
    
def reset(bil1, bil2, inputHasil):
    bil1.set('')
    bil2.set('')
    inputHasil.delete(0, tk.END)

root = tk.Tk()

root.geometry('400x200+500+200')

root.option_add('*font',('verdana',10,'normal'))

root.title("Aritmatika")

labelBilangan1 = tk.Label(root, text="Masukkan Bilangan 1")
labelBilangan1.grid(row=0, column=0, padx=(10,20))
labelBilangan2 = tk.Label(root, text="Masukkan Bilangan 2")
labelBilangan2.grid(row=1, column=0, padx=(10,20) )

bilangan1 = tk.StringVar()
bilangan2 = tk.StringVar()

inputBilangan1 = tk.Entry(root, textvariable=bilangan1)
inputBilangan1.grid(row=0, column=1,padx=(10,20), pady=(5,0))
inputBilangan2 = tk.Entry(root, textvariable=bilangan2)
inputBilangan2.grid(row=1, column=1,padx=(10,20), pady=(5,0))

labelHasil = tk.Label(root, text="Hasil")
labelHasil.grid(row=2, column=0, padx=(10,20), pady=(5,0))

inputHasil = tk.Entry(root)
inputHasil.grid(row=2, column=1,  padx=(10,20), pady=(5,0))


pertambahan = partial(pertambahan, labelHasil, bilangan1, bilangan2, inputHasil)
tombolTambah = tk.Button(root, text="Tambah", command=pertambahan)
tombolTambah.grid(row=3, column=0,  sticky="WE", padx=(10,20), pady=(5,0))
tombolTambah.configure(bg="blue", fg="White")

tombolKurang = tk.Button(root, text="Kurang", command=partial(pengurangan, labelHasil, bilangan1, bilangan2, inputHasil))
tombolKurang.grid(row=3, column=1,  sticky="WE", padx=(10,20), pady=(5,0))
tombolKurang.configure(bg="orange", fg="White")

tombolBagi = tk.Button(root, text="Bagi", command=partial(pembagian, labelHasil, bilangan1, bilangan2, inputHasil))
tombolBagi.grid(row=4, column=0,  sticky="WE", padx=(10,20), pady=(5,0))
tombolBagi.configure(bg="green", fg="White")

tombolKali = tk.Button(root, text="Kali", command=partial(perkalian, labelHasil, bilangan1, bilangan2, inputHasil))
tombolKali.grid(row=4, column=1,  sticky="WE", padx=(10,20), pady=(5,0))
tombolKali.configure(bg="purple", fg="White")

reset = partial(reset, bilangan1, bilangan2, inputHasil)
tombolReset = tk.Button(root, text="Reset", command=reset)
tombolReset.grid(row=5, column=0, columnspan=2, sticky="WE", padx=(10,20), pady=(5,0))
tombolReset.configure(bg="red",fg="White")


root.mainloop()
