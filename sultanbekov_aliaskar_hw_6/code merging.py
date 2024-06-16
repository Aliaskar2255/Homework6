def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Внешний цикл
        for j in range(n - 1 - i):  # Внутренний цикл
            if arr[j] > arr[j + 1]:  # Сравниваем и меняем местами элементы
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, x):
    first = 0
    last = len(arr) - 1
    result_ok = False
    pos = -1

    while first <= last and not result_ok:
        middle = (first + last) // 2
        if arr[middle] == x:
            result_ok = True
            pos = middle
        else:
            if x < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1

    if result_ok:
        print("Элемент найден на позиции:", pos)
    else:
        print("Элемент не найден")


# Применение функций
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

element_to_search = 22
binary_search(sorted_list, element_to_search)
