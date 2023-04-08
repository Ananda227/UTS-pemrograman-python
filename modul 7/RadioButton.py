import tkinter as tk
from functools import partial


def fungsiTampil(labelHasil, rb):
    ambil = rb.get()
    hasil = ambil
    labelHasil.config(text=hasil)
    return

root = tk.Tk()
root.title('ComboBox')
root.geometry('300x200+500+100')

#font digunakan oleh semua widget
root.option_add('*font', ('Verdana', 10, 'normal'))

#font digunakan oleh semua widget label
root.option_add('*Label.font', ('Verdana', 10, 'bold'))

labelPilihOperator = tk.Label(root, text="Pilih Jurusan")
labelPilihOperator.grid(row=0, column=0, sticky="w", padx=(5,0), pady=(5,5))

rbValue = tk.IntVar()
rbSI = tk.Radiobutton(root, text="Sistem Informasi", variable=rbValue, value=1)
rbSI.grid(row=1, column=0, sticky="W")
rbIF = tk.Radiobutton(root, text="Teknik Informatika", variable=rbValue, value=2)
rbIF.grid(row=2, column=0, sticky="W")
rbKA = tk.Radiobutton(root, text="Komputer Akuntasi", variable=rbValue, value=3)
rbKA.grid(row=3, column=0, sticky="W")

labelHasil = tk.Label(root)
labelHasil.grid(row=5, column=0)

tampil = partial(fungsiTampil, labelHasil, rbValue)
tombolTampil = tk.Button(root, text="Tampil", command=tampil)
tombolTampil.grid(row=4, column=0, sticky="WE", padx=(5,0))
tombolTampil.configure(bg="#000", fg="#FFF")
root.mainloop()