print("doan van quyen")
print("235752021610047")
import turtle
import random

# Danh sách các màu sắc
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Tạo đối tượng turtle
painter = turtle.Turtle()
painter.pensize(3)  # Đặt độ dày nét vẽ

# Vẽ 10 vòng tròn với màu ngẫu nhiên
for i in range(12):
    color = random.choice(colors)  # Chọn một màu ngẫu nhiên từ danh sách
    painter.pencolor(color)  # Đặt màu cho bút vẽ
    painter.circle(100)  # Vẽ một hình tròn với bán kính 100
    painter.right(30)  # Quay bút phải 30 độ
    painter.left(60)  # Quay bút trái 60 độ
    painter.setposition(0, 0)  # Đưa bút về vị trí gốc (0, 0)

# Hoàn tất chương trình
turtle.done()
