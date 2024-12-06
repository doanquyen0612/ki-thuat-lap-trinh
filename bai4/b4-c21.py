print ("Sinh vien:Doan Van Quyen MSV:235752021610047")
# Nhập chuỗi số nhị phân từ người dùng
binary_numbers = input("Nhập chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")

# Tách các số nhị phân thành danh sách
binary_list = binary_numbers.split(',')

# Danh sách để lưu các số chia hết cho 5
result = []

# Duyệt qua từng số nhị phân trong danh sách
for binary in binary_list:
    # Chuyển đổi số nhị phân sang số thập phân
    decimal_value = int(binary, 2)
    # Kiểm tra xem có chia hết cho 5 không
    if decimal_value % 5 == 0:
        result.append(binary)

# In kết quả các số chia hết cho 5, phân tách bởi dấu phẩy
print(",".join(result))
