print("doan van quyen")
print("235752021610047")
import tkinter as tk
import random

# List of possible colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

# Initialize score and game time
score = 0
timeleft = 120  # Thay đổi thời gian chơi từ 30 giây thành 120 giây

# Function to start the game
def startGame(event):
    global timeleft
    if timeleft == 120:  # Nếu thời gian là 120, bắt đầu countdown và game
        countdown()
        nextColour()

# Function to choose and display the next colour
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()  # Làm cho ô nhập liệu được kích hoạt

        # Kiểm tra xem người chơi nhập đúng màu hay không
        if e.get().lower() == colours[1].lower():
            score += 2  # Mỗi lần đoán đúng được cộng 2 điểm
        else:
            score -= 1  # Mỗi lần đoán sai sẽ bị trừ 1 điểm

        e.delete(0, tk.END)  # Xóa nội dung trong ô nhập liệu

        random.shuffle(colours)  # Trộn lại danh sách các màu
        label.config(fg=str(colours[1]), text=str(colours[0]))  # Cập nhật màu và từ
        scoreLabel.config(text="Score: " + str(score))  # Cập nhật điểm số

# Countdown timer function
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1  # Giảm thời gian đi 1 giây
        timeLabel.config(text="Time left: " + str(timeleft))  # Cập nhật thời gian còn lại
        timeLabel.after(1000, countdown)  # Gọi lại hàm countdown sau 1 giây

# Driver code
# Tạo cửa sổ GUI
root = tk.Tk()
root.title("COLORGAME")  # Tiêu đề cửa sổ
root.geometry("375x250")  # Kích thước cửa sổ

# Thêm nhãn hướng dẫn
instructions = tk.Label(root, text="Type in the colour of the words, and not the word text!",
                        font=('Helvetica', 12))
instructions.pack()

# Thêm nhãn điểm số
scoreLabel = tk.Label(root, text="Press Enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# Thêm nhãn thời gian còn lại
timeLabel = tk.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Thêm nhãn hiển thị màu
label = tk.Label(root, font=('Helvetica', 60))
label.pack()

# Thêm ô nhập liệu để người chơi nhập màu
e = tk.Entry(root)
e.pack()

# Thực hiện hàm startGame khi người chơi nhấn phím Enter
root.bind('<Return>', startGame)

# Đặt tiêu điểm vào ô nhập liệu
e.focus_set()

# Khởi chạy GUI
root.mainloop()
