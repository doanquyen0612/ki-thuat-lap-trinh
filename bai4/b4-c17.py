print ("sinh vien:Doan Van Quyen MSV:235752021610047")
def sum_of_divisors(x):
    total = 1 
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            total += i
            if i != x // i:
                total += x // i
    return total
def find_abundant_numbers(n):
    abundant_numbers = []
    for num in range(2, n):
        if sum_of_divisors(num) > num:
            abundant_numbers.append(num)
    return abundant_numbers
n = int(input("Nhập số n: "))
print("Các số nguyên dương nhỏ hơn n có tổng các ước số lớn hơn chính nó", n, "là:", find_abundant_numbers(n))
