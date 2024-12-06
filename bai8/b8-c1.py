print("doan van quyen")
print("235752021610047")
import turtle

# Thiết lập màn hình
window = turtle.Screen()
window.bgcolor("lightgreen")  # Đặt màu nền cho cửa sổ

# Tạo đối tượng turtle
painter = turtle.Turtle()
painter.fillcolor('blue')  # Đặt màu lấp đầy
painter.pencolor('blue')  # Đặt màu bút vẽ
painter.pensize(3)  # Đặt độ dày của bút

# Hàm vẽ hình vuông
def drawsq(t, s):
    for i in range(4):  # Lặp lại 4 lần để vẽ 4 cạnh
        t.forward(s)  # Di chuyển về phía trước
        t.left(90)  # Quay trái 90 độ

# Vẽ hình xoáy từ các hình vuông
for i in range(1, 180):  # Lặp để tạo hiệu ứng xoay
    painter.left(18)  # Quay trái một góc nhỏ
    drawsq(painter, 200)  # Gọi hàm vẽ hình vuông với kích thước cạnh là 200

# Kết thúc
turtle.done()
