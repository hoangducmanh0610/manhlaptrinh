
a = int(input("Nhap so nguyen n "))

n1, n2 = 0, 1
count = 0

if a <= 0:
   print("Vui long nhap mot so nguyen duong")
elif a == 1:
   print("Chuỗi Fibonacci tối đa",a,":")
   print(n1)
else:
   print("Chuỗi Fibonacci:")
   while count < a:
       print(n1)
       nth = n1 + n2
    
       n1 = n2
       n2 = nth
       count += 1
