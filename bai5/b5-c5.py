print ("sinh vien: Doan Van Quyen MSV:235752021610047")

import mymodule
n = int(input("nhap so luong phan tu trong danh sach: "))
numbers = []
for i in range(n):
    value = float(input(f"nhap gia tri phan tu thu {i+1}: "))
    numbers.append(value)
max_value, min_value = mymodule.find_max_min(numbers)
sorted_numbers = mymodule.sort_list(numbers)
print(f"gia tri lon nhat: {max_value}")
print(f"gia tri nho nhat: {min_value}")
print(f"danh sach da sap xep: {sorted_numbers}")

  
