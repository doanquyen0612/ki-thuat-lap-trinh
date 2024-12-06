print("doan van quyen")
print("235752021610047")
from tkinter import *

def create_personal_info_form():
    root = Tk()
    root.title("Personal Information")

    # Tạo các nhãn và ô nhập thông tin
    Label(root, text="Họ và tên:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=W)
    Entry(root, width=30).grid(row=0, column=1, padx=10, pady=5)

    Label(root, text="Ngày tháng năm sinh:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=W)
    Entry(root, width=30).grid(row=1, column=1, padx=10, pady=5)

    Label(root, text="MSSV:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky=W)
    Entry(root, width=30).grid(row=2, column=1, padx=10, pady=5)

    Label(root, text="Ngành học:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky=W)
    Entry(root, width=30).grid(row=3, column=1, padx=10, pady=5)

    # Nút thoát
    Button(root, text="Thoát", command=root.quit, font=("Arial", 12)).grid(row=4, column=1, pady=10)

    root.mainloop()

create_personal_info_form()
