print("doan van quyen")
print("235752021610047")
# File: main.py

from search_module import Sequential_Search

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị của danh sách
dlist = []
for i in range(n):
    value = int(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    dlist.append(value)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Thực hiện tìm kiếm
found, index = Sequential_Search(dlist, item)

# In kết quả
if found:
    print(f"Phần tử {item} được tìm thấy tại chỉ mục {index}.")
else:
    print(f"Phần tử {item} không được tìm thấy trong danh sách.")
