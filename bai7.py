#-Nhập 1 list các số nguyên. Tìm ước số chung lớn nhất của list. Tìm bội số chung nhỏ nhất của các số trong list
import math
n=int(input("Nhap so phan tu:"))
a=[int(input("Nhap phan tu:")) for i in range(n)]
ucln=math.gcd(*a)
print(ucln)
bcnn=math.prod(a)//ucln
print(bcnn)