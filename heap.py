  # реализация структуры данных Heap(куча)
def add_to_heap(heap, element):
    """ Добавляет элемент в кучу
    :param heap: list
    :param element: any comparable
    """
    heap.append(element)
    i = len(heap) - 1
    while i > 0 and heap[(i - 1) // 2] < element:
        heap[i] = heap[(i - 1) // 2]
        i = (i - 1) // 2
        heap[i] = element

def pop_from_heap(heap):
    """ Возвращает наибольший элемент из кучи (с самого верха)
    :param heap: list
    """
    if len(heap) == 1:
        return heap.pop()
    element = heap[0]
    heap[0] = heap.pop()
    i = 0
    while 2 * i + 2 < len(heap) and heap[i] < max(heap[2 * i + 1], heap[2 * i + 2]):
        if heap[2 * i + 1] > heap[2 * i + 2]:
            heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
            i = 2 * i + 1
        else:
            heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]
            i = 2 * i + 2
    if 2 * i + 1 == len(heap) - 1 and heap[i] < heap[2 * i + 1]:
        heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
    return element


heap = []
add_to_heap(heap, 25)
add_to_heap(heap, 15)
add_to_heap(heap, 2)
add_to_heap(heap, 8)
add_to_heap(heap, 40)
add_to_heap(heap, 9)
add_to_heap(heap, 0)
add_to_heap(heap, 24)
add_to_heap(heap, 11)
print(heap)
print(pop_from_heap(heap))
print(pop_from_heap(heap))
print(pop_from_heap(heap))
print(pop_from_heap(heap))
print(pop_from_heap(heap))
print(heap)
add_to_heap(heap, 11)
add_to_heap(heap, 15)
add_to_heap(heap, 3)
add_to_heap(heap, 2)
print(heap)