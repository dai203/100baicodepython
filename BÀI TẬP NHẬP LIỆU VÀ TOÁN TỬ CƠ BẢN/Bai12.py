# Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c
# Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
c = int(input("Nhập vào số c: "))

d = (a + b)**c 
kq = 100 <= d <=200
print(kq)

