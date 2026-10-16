# 3.1listbox

import tkinter as tk
cua_so = tk.Tk()
cua_so.title("vi du listbox")
cua_so.geometry("400x300")
listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single")
for mon in ["toan","ly","hoa","van","anh"]:
    listbox_mon_hoc.insert(tk.END, mon)
listbox_mon_hoc.pack(pady=15)
def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()
    if lua_chon:
        nhan_ket_qua.config(text=f"mon da chon : {listbox_mon_hoc.get(lua_chon[0])}")
tk.Button(cua_so, text="xem mon da chon", command=xem_mon_da_chon).pack(pady=15)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()


#3.2 Combobox
import tkinter as tk
from tkinter import ttk
cua_so = tk.Tk()
cua_so.title("vi du combobox")
cua_so.geometry("300x180")
tk.Label(cua_so, text="Chon thanh pho:").pack(pady=10)
combobox_thanh_pho = ttk.Combobox(cua_so, values=["HA NOI","DA NANG","HCM","HUE","THANH HOA"])
combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=15)
def xem_thanh_pho():
    nhan_ket_qua.config(text=f"Ban chon: {combobox_thanh_pho.get()}")
tk.Button(cua_so, text="Xac nhan", command=xem_thanh_pho).pack(pady=10)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()
cua_so.mainloop()



