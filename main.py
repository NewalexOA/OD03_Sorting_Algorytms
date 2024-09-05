def bubble_sort(arr):
    """
    Сортировка пузырьком: многократный проход по массиву, 
    на каждом из которых соседние элементы сравниваются и меняются местами, 
    если они находятся в неправильном порядке.
    """
    n = len(arr)
    # Проход по всем элементам массива
    for run in range(n-1):
        # Внутренний проход для сравнения и обмена элементов
        for i in range(n-1-run):
            if arr[i] > arr[i + 1]:
                # Обмен элементов, если они в неправильном порядке
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Пример использования:
arr = [5, 7, 4, 3, 8, 2]
bubble_sort(arr)
print(arr)

def quick_sort(arr):
    """
    Быстрая сортировка: рекурсивный алгоритм, который использует метод "разделяй и властвуй".
    Выбирается опорный элемент, и массив делится на две части: элементы меньше опорного и элементы больш�� или равны опорному.
    """
    # Базовый случай для рекурсии
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    # Разделение массива на две части
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    # Рекурсивная сортировка и объединение
    return quick_sort(left) + [pivot] + quick_sort(right)

# Пример использования:
arr = [5, 7, 4, 3, 8, 2]
print(quick_sort(arr))

def selection_sort(arr):
    """
    Сортировка выбором: на каждом шаге выбирается минимальный элемент из неотсортированной части массива 
    и меняется местами с первым элементом неотсортированной части.
    """
    # Проход по всем элементам массива
    for i in range(len(arr)):
        min_index = i
        # Поиск минимального элемента в оставшейся части массива
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Обмен найденного минимального элемента с текущим
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Пример использования:
arr = [-3, 5, 0, -8, 1, 10]
selection_sort(arr)
print(arr)

def insertion_sort(arr):
    """
    Сортировка вставками: элементы массива просматриваются по одному, 
    и каждый новый элемент вставляется в уже отсортированную часть массива на правильное место.
    """
    # Проход по всем элементам массива, начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещение элементов, которые больше ключа, на одну позицию вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставка ключа на правильную позицию
        arr[j + 1] = key

# Пример использования:
arr = [-3, 5, 0, -8, 1, 10]
insertion_sort(arr)
print(arr)