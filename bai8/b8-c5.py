print("doan van quyen")
print("235752021610047")
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# Khai báo biến để lưu trữ lựa chọn của người dùng
v = tk.IntVar()
v.set(1)  # Gán giá trị mặc định là Python (giá trị 1)

# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm hiển thị lựa chọn của người dùng
def ShowChoice():
    print("Lựa chọn của bạn là:", v.get())

# Cấu hình lựa chọn giữa RadioButton thông thường và indicator
use_indicator = True  # Đặt False để sử dụng RadioButton thông thường

# Thêm nhãn giới thiệu cho các button
tk.Label(root,
         text="""Choose your favourite
programming language:""",
         justify=tk.LEFT,
         padx=20).pack()

# Tạo các button với kiểu RadioButton hoặc Indicator dựa trên cấu hình
for language, val in languages:
    if use_indicator:
        # Dùng indicator (nút bấm thay vì radio button)
        tk.Radiobutton(root,
                       text=language,
                       indicatoron=0,  # Đặt indicatoron = 0 để hiển thị dưới dạng button
                       width=20,       # Điều chỉnh độ rộng của nút
                       padx=20,        # Thêm khoảng cách bên trái cho văn bản
                       variable=v,
                       command=ShowChoice,
                       value=val).pack(anchor=tk.W)
    else:
        # Dùng RadioButton thông thường
        tk.Radiobutton(root,
                       text=language,
                       padx=20,
                       variable=v,
                       command=ShowChoice,
                       value=val).pack(anchor=tk.W)

# Bắt đầu vòng lặp chính để hiển thị giao diện
root.mainloop()
