#tạo list số chẵn, lẻ
chan=[]
le=[]
while True:    #tạo vòng lặp để nhập lại khi xảy ra lỗi
    try:
        a=input('Nhập mảng m bất kỳ: ').split()
        #nhap vào một mảng m bất kì cách nhau bởi dấu cách

        for i in range(0, len(a)):
              a[i]=int(a[i])
        #đưa dạng str về int
        for u in a:
        #tìm số chẵn,lẻ thêm vào list
            if u%2==0:
                chan.append(u)
                   
            else:
                le.append(u)
        print('so chan la: ',chan)
        print('so le la: ',le)
        b=sum(chan)/len(chan)#tính trung bình cộng số chẵn
        print('trung binh cong so chan la: ',b)
        break
    except ZeroDivisionError:
    #thông báo lỗi hàm sum khi không có số chẵn thông báo với người dùng và break ra
        print('Không có số chẵn trong mảng!')
        break
    except:
    #thông báo các lỗi còn lại không break để tiếp tục chạy lại vòng while
        print('Lỗi giá trị!hãy nhập lại!')
 
    
