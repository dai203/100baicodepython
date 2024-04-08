# Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
a = float(input("Nhập vào độ dài cạnh a: "))
b = float(input("Nhập vào độ dài cạnh b: "))
c = float(input("Nhập vào độ dài cạnh c: "))
def kt(a, b, c):
    # Kiểm tra điều kiện ba cạnh
    if a + b > c and a + c > b and b + c > a:
        # Kiểm tra điều kiện độ dài các cạnh lớn hơn 0
        if a > 0 and b > 0 and c > 0:
            return True
    return False


# Kiểm tra xem ba cạnh có tạo thành một tam giác không
if kt(a, b, c):
    print("Ba cạnh đã nhập có thể tạo thành một tam giác.")
else:
    print("Ba cạnh đã nhập không thể tạo thành một tam giác.")
