import time
import random


def sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, time.time() - start_time


def ordered_sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found, time.time() - start_time


def binary_search_iterative(a_list, item):
    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, time.time() - start_time


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)


def binary_search_recursive_wrap(a_list, item):
    start_time = time.time()
    result = binary_search_recursive(a_list, item)
    return result, time.time() - start_time

def main():
    a_time = 0.0
    b_time = 0.0
    c_time = 0.0
    d_time = 0.0
    for number in range(100):
        my_randoms = random.sample(range(50000), 10000)
        my_randoms.sort()
        a = sequential_search(my_randoms,-1)
        a_time = a_time + a[1]
        b = ordered_sequential_search(my_randoms, -1)
        b_time = b_time + b[1]
        c = binary_search_iterative(my_randoms, -1)
        c_time = c_time + c[1]
        d = binary_search_recursive_wrap(my_randoms, -1)
        d_time = d_time + d[1]
    # print(a)
    a_time= a_time / 100.0
    b_time = b_time / 100.0
    c_time = c_time / 100.0
    d_time = d_time / 100.0
    print("Sequential Search took %10.7f seconds to run, on average" % a_time)
    print("Ordered Sequential Search took %10.7f seconds to run, on average" % b_time)
    print("Binary Search Iterative took %10.7f seconds to run, on average" % c_time)
    print("Binary Search Recursive took %10.7f seconds to run, on average" % d_time)

if __name__ == "__main__":
    main()


