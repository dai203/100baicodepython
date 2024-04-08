# Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, 
# kiểm tra xem đó là tam giác gì (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường
# Nhập độ dài các cạnh từ người dùng
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

def kt1(a, b, c):
    if kt(a, b, c):
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or a == c:
            if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
                return "Tam giác vuông cân"
            else:
                return "Tam giác cân"
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"
    else:
        return "Ba cạnh không thể tạo thành tam giác"


# Kiểm tra và in ra loại tam giác hoặc thông báo
print("Loại tam giác là:", kt1(a, b, c))
