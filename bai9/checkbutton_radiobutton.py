#hoat dong 1

import tkinter as tk


cua_so = tk.Tk()
cua_so.title("vi du check button")
cua_so.geometry("400x300")
tk.Label(cua_so, text="chon so thich cua ban:", font=("Arial",15)).pack(pady=10)
bien_doc_sach = tk.BooleanVar()
bien_the_thao = tk.BooleanVar()
bien_am_nhac = tk.BooleanVar()
tk.Checkbutton(cua_so, text="doc sach" , variable=bien_doc_sach).pack(anchor="w",padx=30)
tk.Checkbutton(cua_so ,text="the thao" , variable=bien_the_thao).pack(anchor="w",padx=30)
tk.Checkbutton(cua_so, text="am nhac" , variable=bien_am_nhac).pack(anchor="w",padx=30)
def xem_lua_chon():
    print("doc sach:",bien_doc_sach.get())
    print("the thao:",bien_the_thao.get())
    print("am nhac:",bien_am_nhac.get())
tk.Button(cua_so, text="lua chon" , #in ra console
command=xem_lua_chon).pack(pady=15)
cua_so.mainloop()

#hoat dong 2 : Radiobutton
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("vi du check radibutton")
cua_so.geometry("400x300")
bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")
tk.Label(cua_so, text="loai tai khoan: ", font=("Arial",15)).pack(pady=15)
tk.Radiobutton(cua_so, text="Ca nhan", variable=bien_loai_tai_khoan, value="ca_nhan").pack(anchor="w", padx=30)
tk.Radiobutton(cua_so, text="Doanh nghiep", variable=bien_loai_tai_khoan, value="doanh_nghiep").pack(anchor="w", padx=30)
def xem_loai_tai_khoan():
    nhan_ket_qua.config(text=f"Ban da chon: {bien_loai_tai_khoan.get()}")
tk.Button(cua_so, text="xac nhan", command=xem_loai_tai_khoan).pack(pady=15)
nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 15) )
nhan_ket_qua.pack(pady=10)

cua_so.mainloop()
