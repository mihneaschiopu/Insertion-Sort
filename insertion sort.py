# insertion sort


nlist = [57, 92, 93, 67, 41, 21, 9]


# external loop beginning at one (1) 
for index in range (1, len(nlist)):


    # data item needs to be compared
    current = nlist[index]
    index2 = index


    # internal loop
    while (index2 > 0 and nlist[index2 - 1] > current):
        print(f"Value compared to current: {nlist[index2-1]}")
        print(f"Index2 value: {index2}")
        print(f"Current Value: {current} \n\n")

        nlist[index2] = nlist[index2-1]
        index2 = index2 - 1
        print(nlist)
    nlist[index2] = current




print(nlist)



    
    


    

    

