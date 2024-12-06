print("doan van quyen")
print("235752021610047")
from tkinter import *

def create_radio_button_form():
    def on_click():
        selected = var.get()
        lbl_result.config(text=f"Bạn đã chọn: {selected}")

    root = Tk()
    root.title("Radio Button Example")

    # Tạo nhãn "Welcome"
    Label(root, text="Welcome", font=("Arial", 14)).pack(pady=10)

    # Tạo Radio Buttons
    var = StringVar(value="1")  # Giá trị mặc định là "1"
    frame = Frame(root)
    frame.pack()

    Radiobutton(frame, text="First", variable=var, value="1", font=("Arial", 12)).pack(side=LEFT, padx=5)
    Radiobutton(frame, text="Second", variable=var, value="2", font=("Arial", 12)).pack(side=LEFT, padx=5)
    Radiobutton(frame, text="Third", variable=var, value="3", font=("Arial", 12)).pack(side=LEFT, padx=5)

    # Nút "Click Me"
    Button(root, text="Click Me", command=on_click, font=("Arial", 12)).pack(pady=10)

    # Nhãn hiển thị kết quả
    lbl_result = Label(root, text="", font=("Arial", 12))
    lbl_result.pack()

    root.mainloop()

create_radio_button_form()
