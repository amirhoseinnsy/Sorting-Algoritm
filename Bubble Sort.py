list1 = [2, 5, 3, 8, 6, 1]


def sort_t_f(*args):
    list2 = args[0]
    temp_2 = 0
    for i in range(len(list2)):
        if i != 0:
            if temp_2 > list2[i]:
                return False
        temp_2 = list2[i]

    return True


temp = 0

while sort_t_f(list1) == 0:
    for i in range(len(list1)):
        if i != 0:
            if list1[i] < temp:
                temp_3 = list1[i]
                list1[i] = temp
                list1[i - 1] = temp_3
                print(list1)

        temp = list1[i]

# print(list1)
