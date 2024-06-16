def binary_search(lst, x):
    first = 0
    last = len(lst) - 1
    result_ok = False
    pos = -1

    while first <= last and not result_ok:
        middle = (first + last) // 2
        if lst[middle] == x:
            result_ok = True
            pos = middle
        else:
            if x < lst[middle]:
                last = middle - 1
            else:
                first = middle + 1

    if result_ok:
        print("Элемент найден на позиции:", pos)
    else:
        print("Элемент не найден")
