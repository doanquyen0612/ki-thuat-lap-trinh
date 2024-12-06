print ("doan van quyen")
print ("235752021610047")

# File: main.py

from search_module import binary_search

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị của danh sách
dlist = []
for i in range(n):
    value = int(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    dlist.append(value)

# Sắp xếp danh sách trước khi tìm kiếm
dlist.sort()

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Thực hiện tìm kiếm
found = binary_search(dlist, value)

# In kết quả
if found:
    print(f"Phần tử {value} được tìm thấy trong danh sách.")
else:
    print(f"Phần tử {value} không được tìm thấy trong danh sách.")
