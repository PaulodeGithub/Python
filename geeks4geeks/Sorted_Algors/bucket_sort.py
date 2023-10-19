def buckerSort(x):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])
        print(arr)

    for j in x:
        index_arr = int(slot_num * j)
        arr[index_arr].append(j)

    for i in range(slot_num):
        arr[i] = insert_sort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k +=1

    return x

