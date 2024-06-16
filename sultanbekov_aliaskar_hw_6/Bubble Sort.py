def bubble_sort(one):
    n = len(one)
    for i in range(n-1):  # Внешний цикл
        for j in range(n-1-i):  # Внутренний цикл
            if one[j] > one[j+1]:  # Сравниваем и меняем местами элементы
                one[j], one[j+1] = one[j+1], one[j]
    return one

# Применение функции bubble_sort
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)
