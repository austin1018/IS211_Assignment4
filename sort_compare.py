import time
import random

def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    return time.time() - start_time

def shell_sort(a_list):
    start_time = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    return time.time() - start_time

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position>= gap and a_list[position - gap]>current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

def python_sort(a_list):
    start_time = time.time()
    a_list.sort()
    return time.time() - start_time

def main():
    a_time = 0.0
    b_time = 0.0
    c_time = 0.0
    my_randoms1 = random.sample(range(50000), 1000)
    my_randoms2 = random.sample(range(50000), 1000)
    my_randoms3 = random.sample(range(50000), 1000)
    a_time = insertion_sort(my_randoms1)
    b_time = shell_sort(my_randoms2)
    c_time = python_sort(my_randoms3)
    # print(a)
    print("Insertion sort took %10.7f seconds to run" % a_time)
    print("Shell sort took %10.7f seconds to run" % b_time)
    print("Python sort took %10.7f seconds to run" % c_time)

if __name__ == "__main__":
    main()
