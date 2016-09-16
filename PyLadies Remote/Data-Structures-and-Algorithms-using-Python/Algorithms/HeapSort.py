from random import randint


def heap_sort(input_list):
    last = len(input_list)
    first = last // 2 - 1
    for i in range(first, -1, -1):
        heapify(input_list, last, i)
    for i in range(last - 1, 0, -1):
        swap(input_list, i, 0)
        heapify(input_list, i, 0)
    return input_list


def heapify(input_list, last, i):
    left_child = 2 * i + 1
    right_child = 2 * (i + 1)
    max = i
    if left_child < last and input_list[i] < input_list[left_child]:
        max = left_child
    if right_child < last and input_list[max] < input_list[right_child]:
        max = right_child
    if max != i:
        swap(input_list, i, max)
        heapify(input_list, last, max)


def swap(input_list, i, j):
    input_list[i], input_list[j] = input_list[j], input_list[i]


input_list = [randint(1, 10) for i in range(10)]
print input_list
sorted_list = heap_sort(input_list)
print sorted_list
