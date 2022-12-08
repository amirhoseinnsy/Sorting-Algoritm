temp = [2, 4, 7, 9, 5, 0, 8]


def find_min(*args):
    list_1 = args[0]
    value = list_1[0]
    index = 0
    for i in range(len(list_1)):
        if value > list_1[i]:
            value = list_1[i]
            index = i
    return index


for i in range(len(temp)):
    min_index = find_min(temp[i: len(temp)]) + i
    temp_2 = temp[i]
    temp[i] = temp[min_index]
    temp[min_index] = temp_2

print(temp)
