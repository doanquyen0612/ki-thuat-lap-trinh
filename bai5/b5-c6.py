print ("sinh vien: Doan Van Quyen MSV:235752021610047")

import mymodule
n = int(input("Nhập số lượng phần tử trong danh sách: "))
numbers = []
for i in range(n):
    value = float(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    numbers.append(value)
max_value, min_value = mymodule.find_max_min(numbers)
max_index = numbers.index(max_value)
min_index = numbers.index(min_value)
sorted_numbers = mymodule.sort_list(numbers)
print(f"Giá trị lớn nhất: {max_value} tại vị trí {max_index}")
print(f"Giá trị nhỏ nhất: {min_value} tại vị trí {min_index}")
print(f"Danh sách đã sắp xếp: {sorted_numbers}")
