import tkinter as tk
from tkinter.ttk import Style, Frame
from tkinter import ttk

root=tk.Tk()

root.geometry("640x400")

root.columnconfigure(0, pad=4)

root.title("Đăng ký thông tin")

name_var=tk.StringVar()
mssv_var=tk.StringVar()
ngaySinh_var = tk.StringVar()
email_var = tk.StringVar()
sdt_var = tk.StringVar()
hk_var = tk.StringVar()

lblMain = tk.Label(text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", foreground='red').grid(row = 0, column=2, pady=20, sticky="W")

lbl_mssv = tk.Label(text="Mã số sinh viên").grid(row = 1, column=1, sticky="W")
mssv_entry = tk.Entry(root, textvariable=mssv_var, width=60).grid(row=1, column=2, sticky="W")

lbl_name = tk.Label(text="Họ và tên sinh viên").grid(row = 2, column=1, sticky="W")
name_entry = tk.Entry(root, textvariable=name_var, width=60).grid(row = 2, column=2, sticky="W")

lbl_ngaySinh = tk.Label(text="Ngày sinh").grid(row=3, column=1, sticky="W")
ngaySinh_entry = tk.Entry(root, textvariable=ngaySinh_var, width=60).grid(row=3, column=2, sticky="W")

lbl_email = tk.Label(text="Email").grid(row=4, column=1, sticky="W")
email_entry = tk.Entry(root, textvariable=email_var, width=60).grid(row=4,column=2, sticky="W")

lbl_sdt = tk.Label(text="Số điện thoại").grid(row = 5, column=1, sticky="W")
sdt_entry = tk.Entry(root, textvariable=sdt_var, width=60).grid(row = 5, column=2, sticky="W")

lbl_hk = tk.Label(text="Học kỳ").grid(row=6, column=1, sticky="W")
hk_entry = tk.Entry(root, textvariable=hk_var, width=60).grid(row = 6, column= 2, sticky="W")

lbl_namHoc = tk.Label(text="Năm học").grid(row=7, column=1, sticky="W")

n = tk.StringVar()
namHoc_cbb = ttk.Combobox(root, width=57, textvariable=n)
namHoc_cbb['values']= ('2021', '2022', '2023', '2024')
namHoc_cbb.current(0)
namHoc_cbb.grid(row = 7, column=2, sticky="W")

lbl_chonMon = tk.Label(text="Chọn môn học").grid(row = 8, column=1, sticky="W")
py_check = tk.Checkbutton(text="Lập trình Python").grid(row = 9, column=2, sticky="W")
jav_check = tk.Checkbutton(text="Lập trình Java").grid(row = 9, column=3, sticky="W")
cnpm_check = tk.Checkbutton(text="Công nghệ phần mềm").grid(row = 10, column=2, sticky="W")
ptudw_check = tk.Checkbutton(text="Phát triển ứng dụng Web").grid(row = 10, column=3, sticky="W")

root.mainloop()