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

data = [5, 3, 13, 1, 12, 29, 11]

#ModifiedSortingMinMax
data = [5, 3, 13, 1, 12, 29, 11]   
print("Data awal =", data)
print("")
iterasi=1
minim=0
maksim=len(data)-1
while minim < maksim:
    print("Iterasi ke-",iterasi)
    indexmin=minim
    for k in range(minim+1,maksim+1):
        if data[indexmin]>data[k]:
            indexmin=k
    data[minim],data[indexmin]=data[indexmin],data[minim]
    print("minimum", data)
    indexmax=maksim
    for j in range(maksim-1,minim-1,-1):
        if data[j]>data[indexmax]:
            indexmax=j
    data[maksim],data[indexmax]=data[indexmax],data[maksim]
    print("maksimum", data)
    print("")
    minim+=1
    maksim-=1
    iterasi+=1
print("Data terurut =", data)
print(" ")
print(" ")
data = [5, 3, 13, 1, 12, 29, 11]
ModifiedSortingDescending(data, 'max')
ModifiedSortingAscending(data, 'max')
