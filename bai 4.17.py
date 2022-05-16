n=int(input("Nhập N=:"))
for i in range(2,n):
    s=0
    #lấy các số nhỏ hơn i
    for j in range(1,i):
        #tìm ước của i
        if(i%j == 0):
            s = s + j
    if(s>i):
        print(i)
        
