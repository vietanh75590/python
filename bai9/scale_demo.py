#hoat dong 4
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("vi du scale")
cua_so.geometry("500x400")
def khi_keo_thanh_truot(gia_tri):
    nhan_gia_tri.config(text=f"Gia tri hien tai: {gia_tri}")
thanh_truot = tk.Scale(cua_so, from_=0, to=100, orient="horizontal", command=khi_keo_thanh_truot)
thanh_truot.pack(pady=20, fill="x", padx=20)
nhan_gia_tri = tk.Label(cua_so, text="Gia tri hien tai: 0", font=("Arial", 12))
nhan_gia_tri.pack()

cua_so.mainloop()