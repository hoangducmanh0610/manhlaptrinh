def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

mystr = input("Nhập các phần tử của dãy số cách nhau bởi dấu cách: ")
mylist = mystr.split()
nlist = [int(i) for i in mylist]

bubbleSort(nlist)
print(nlist)
