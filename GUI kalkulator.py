import tkinter as tk
from tkinter import ttk

# Fungsi untuk mengupdate nilai pada entry hasil
def update_hasil(nilai):
    current = entry_hasil.get()
    entry_hasil.delete(0, tk.END)
    entry_hasil.insert(tk.END, current + nilai)

# Fungsi untuk menghitung hasil
def hitung():
    try:
        hasil = eval(entry_hasil.get())
        entry_hasil.delete(0, tk.END)
        entry_hasil.insert(0, str(hasil))
    except ZeroDivisionError:
        entry_hasil.delete(0, tk.END)
        entry_hasil.insert(0, "Error")
    except Exception as e:
        entry_hasil.delete(0, tk.END)
        entry_hasil.insert(0, "Error")

# Fungsi untuk menghapus nilai pada entry hasil
def hapus():
    entry_hasil.delete(0, tk.END)

# Membuat window
window = tk.Tk()
window.title("Kalkulator")

# Membuat entry untuk menampilkan hasil
entry_hasil = tk.Entry(width=25, font=('Arial', 14), justify='right')
entry_hasil.grid(row=0, column=0, columnspan=4)

# Membuat tombol-tombol angka
for i in range(9):
    tombol = ttk.Button(text=str(i+1), command=lambda i=i: update_hasil(str(i+1)))
    tombol.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)

# Membuat tombol angka 0
tombol_0 = ttk.Button(text='0', command=lambda: update_hasil('0'))
tombol_0.grid(row=4, column=1, padx=5, pady=5)

# Membuat tombol operator
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    tombol_operator = ttk.Button(text=operator, command=lambda operator=operator: update_hasil(operator))
    tombol_operator.grid(row=i+1, column=3, padx=5, pady=5)

# Membuat tombol hasil
tombol_hasil = ttk.Button(text='=', command=hitung)
tombol_hasil.grid(row=4, column=2, padx=5, pady=5)

# Membuat tombol hapus
tombol_hapus = ttk.Button(text='C', command=hapus)
tombol_hapus.grid(row=4, column=0, padx=5, pady=5)

# Menjalankan event loop
window.mainloop()
