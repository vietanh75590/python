#bai tap 1.1
import tkinter as tk
from struct import pack
from tkinter import font

cua_so = tk.Tk()
cua_so.title("cua so tkinter dau tien")
cua_so.geometry("500x400")


#bai tap 1.2
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("ung dung demo")
cua_so.geometry("400x350")
cua_so.resizable(True,False)
nhan = tk.Label(cua_so, text = "xin chao tkinter !" , font=("Arial" , 16))
nhan.pack(pady=20)


#hoat dong 2
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("vi du frame")
cua_so.geometry("432x321")
khung_tren = tk.Frame(cua_so , bg="lightblue" , height=100)
khung_tren.pack(fill="x")
khung_duoi = tk.Frame(cua_so , bg="lightyellow" )
khung_duoi.pack(fill="both" , expand=True)
tk.Label(khung_tren , text="khu vuc tieu de" , bg="lightblue").pack(pady=10)
tk.Label(khung_duoi , text="khu vuc noi dung" , bg="lightyellow").pack(pady=10)
cua_so.mainloop()