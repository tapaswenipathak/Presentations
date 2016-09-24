from random import randint


def heap_sort(input_list):
    n = len(input_list)
    
    # Build a max heap
    for i in range(n, -1, -1):
        heapify(input_list, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        swap(input_list, i, 0)
        heapify(input_list, i, 0)
    return input_list


def heapify(input_list, last, i):
    left_child = 2 * i + 1
    right_child = 2 * (i + 1)
    max = i #Intialize largest as root
    
    # Check if left child of root exists and is it greater than root
    if left_child < last and input_list[i] < input_list[left_child]:
        max = left_child
    # Check if right child of root exists and is it greater than root
    if right_child < last and input_list[max] < input_list[right_child]:
        max = right_child
    # Change root if max value is changed
    if max != i:
        swap(input_list, i, max)
        # heapify the root
        heapify(input_list, last, max)


def swap(input_list, i, j):
    input_list[i], input_list[j] = input_list[j], input_list[i]


input_list = [randint(1, 10) for i in range(10)]
print input_list
sorted_list = heap_sort(input_list)
print sorted_list
