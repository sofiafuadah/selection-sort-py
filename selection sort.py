def ModifiedSortingAscending(data, select):
    print("Data awal = ",data)
    if select == 'min':
        for i in range(len(data)-1):
            print("Iterasi Ke-{0}".format(i+1))
            minFlag=i
            for j in range(i+1, len(data)):
                if data[minFlag] > data[j]:
                    minFlag=j
            data[i],data[minFlag]=data[minFlag],data[i]
            print(data)
    if select == 'max':
        for i in range(len(data)-1,-1,-1):
            print("Iterasi Ke-{0}".format(len(data)-i))
            maxFlag = i
            for j in range(i-1,-1,-1):
                if data[maxFlag]<data[j]:
                    maxFlag = j
            data[i],data[maxFlag]=data[maxFlag],data[i]
            print(data)
def ModifiedSortingDescending(data, select):
    print("Data awal = ",data)
    if select == 'max':
        for i in range(len(data)-1):
            print("Iterasi Ke-{0}".format(i+1))
            minFlag=i
            for j in range(i+1, len(data)):
                if data[minFlag] < data[j]:
                    minFlag=j
            data[i],data[minFlag]=data[minFlag],data[i]
            print(data)
    if select == 'min':
        for i in range(len(data)-1,-1,-1):
            print("Iterasi Ke-{0}".format(len(data)-i))
            maxFlag = i
            for j in range(i-1,-1,-1):
                if data[maxFlag]>data[j]:
                    maxFlag = j
            data[i],data[maxFlag]=data[maxFlag],data[i]
            print(data)
#ModifiedSortingMinMax
data = [5, 3, 13, 1, 12, 29, 11]   
for i,luar in enumerate(range(len(data)-1,0,-1)):
    bigFlag = luar
    lowFlag = len(data)-luar-1
    urut = True
    print("Iterasi ke -",i)
    for minimal in range(len(data)-luar,len(data)):
        if data[lowFlag] > data[minimal]:
            lowFlag = minimal
    data[len(data)-luar-1],data[lowFlag] = data[lowFlag],data[len(data)-luar-1]
    print("data Minimal =",data)
    for maximal in range(luar-1,-1,-1):
        if data[bigFlag] < data[maximal]:
            bigFlag = maximal
    data[luar],data[bigFlag] = data[bigFlag],data[luar]
    print("data Maximal =",data)
    for cek in range(len(data)-1):
        if data[cek] < data[cek+1]:
            urut = urut and True
        else:
            urut = urut and False
    if urut:
        break
print(" ")
data = [5, 3, 13, 1, 12, 29, 11]
ModifiedSortingDescending(data, 'max')
ModifiedSortingAscending(data, 'max')
