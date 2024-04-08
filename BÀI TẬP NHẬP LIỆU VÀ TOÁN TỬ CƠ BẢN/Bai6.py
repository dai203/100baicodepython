# Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
a = int(input("Nhập vào số nguyên a: "))
kq = (a % 5 == 0) and (20 > a < 70)
print(kq)
