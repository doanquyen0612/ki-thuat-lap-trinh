print("doan van quyen")
print("235752021610047")
from tkinter import *

# Xây dựng cửa sổ đồ họa (window form)
window = Tk()
window.title("Welcome to LikeGeeks app")  # Tiêu đề cửa sổ
window.geometry('350x200')  # Kích thước cửa sổ

# Thêm một widget (Label) vào window form
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)  # Đặt Label tại vị trí (0, 0)

# Phương thức xử lý sự kiện khi nút được bấm
def clicked():
    lbl.configure(text="Button was clicked !!")

# Thêm một widget (Button) vào window form và thay đổi màu nền, màu chữ
btn = Button(window, text="Click Me", command=clicked, bg="blue", fg="white")
btn.grid(column=1, row=0)  # Đặt Button tại vị trí (1, 0)

# Xử lý sự kiện phím bấm (Ví dụ: bấm phím 'a')
def key_pressed(event):
    lbl.configure(text=f"Key '{event.char}' was pressed!")

# Xử lý sự kiện khi phím được nhấn
window.bind('<Key>', key_pressed)

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
