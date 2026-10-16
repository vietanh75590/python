import tkinter as tk

def bam(ky_tu):
    if ky_tu == "=":
        try: bien_hien_thi.set(str(eval(bien_hien_thi.get())))
        except: bien_hien_thi.set("Lỗi")
    elif ky_tu == "C":
        bien_hien_thi.set("")
    else:
        bien_hien_thi.set(bien_hien_thi.get() + ky_tu)
root = tk.Tk()
root.title("Máy tính")
bien_hien_thi = tk.StringVar()

tk.Entry(root, textvariable=bien_hien_thi, font=("Arial", 20), justify="right", width=14).grid(row=0, column=0, columnspan=4, pady=8)
cac_nut = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]
for i, k in enumerate(cac_nut):
    tk.Button(root, text=k, font=("Arial", 15), width=4, height=2,
              command=lambda x=k: bam(x)).grid(row=i//4 + 1, column=i%4, padx=2, pady=2)
root.mainloop()