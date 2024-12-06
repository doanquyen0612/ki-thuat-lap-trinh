print("doan van quyen")
print("235752021610047")
import turtle
import random

# Khởi tạo màn hình và bút vẽ
screen = turtle.Screen()
screen.bgcolor("white")  # Màu nền trắng
painter = turtle.Turtle()  # Tạo đối tượng turtle
painter.pensize(3)  # Đặt độ dày của bút vẽ

# Danh sách màu sắc
colors = ["red", "blue", "green", "orange", "purple"]

# Vẽ các hình tròn như yêu cầu
for i in range(12):
    color = random.choice(colors)  # Chọn một màu ngẫu nhiên từ danh sách
    painter.pencolor(color)  # Đặt màu cho bút vẽ
    painter.circle(100)  # Vẽ một hình tròn bán kính 100
    painter.right(30)  # Quay bút đi 30 độ sau mỗi hình tròn
    painter.setposition(0, 0)  # Đảm bảo bút quay về vị trí (0, 0)

# Hoàn tất vẽ
painter.hideturtle()  # Ẩn bút vẽ sau khi hoàn tất
screen.mainloop()  # Giữ cửa sổ vẽ mở
