from collections import deque, Counter, defaultdict, OrderedDict
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from bisect import bisect_left, bisect_right, insort, bisect
from random import randint, choice, shuffle, sample, random
from math import gcd, factorial, sqrt, ceil, floor, inf, pi
from array import array
from itertools import permutations, combinations, product, accumulate
from functools import cache, lru_cache, partial, reduce

# Standard library functions
from builtins import (
    all,
    sum,
    min,
    max,
    sorted,
    range,
    enumerate,
    zip,
    map,
    filter,
    reversed,
)

# Example code for each algorithm or data structure


def demo_map():
    l = [{"key": key, "val": val} for key, val in enumerate([i**2 for i in range(5)])]
    # Using map correctly to transform each dictionary in the list
    res = list(map(lambda a: a["val"], l))
    print("Mapped values:", res)


def demo_reduce():
    l = [1, 2, 3]
    res = reduce(lambda a, b: a + b, l, 0)
    print("Reduced: ", res)


def demo_list():
    my_list = [3, 1, 4]
    my_list.append(2)
    my_list.sort()
    print("List:", my_list)


def demo_array():
    arr = array("i", [1, 2, 3])
    arr.append(4)
    print("Array:", arr)


def demo_tuple():
    my_tuple = (1, 2, 3)
    print("Tuple:", my_tuple)


def demo_dictionary():
    my_dict = {"a": 1, "b": 2}
    my_dict["c"] = 3
    print("Dictionary:", my_dict)

    my_map = dict()
    my_map[1] = 99
    my_map.get(1)


def demo_set():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print("Set Union:", set1.union(set2))
    print("Set Intersection:", set1 & set2)


def demo_deque():
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.pop()
    print("Deque:", dq)


def demo_counter():
    cnt = Counter("abacaba")
    print("Counter:", cnt.most_common(1))


def demo_defaultdict():
    # defaultdict automatically creates default values for missing keys
    # avoiding KeyError when accessing non-existent keys
    # useful for graphs, frequency counters, and grouping data
    graph = defaultdict(list)
    graph[0].append(1)  # No KeyError even though key 0 didn't exist before
    print("Defaultdict:", graph)


def demo_ordereddict():
    od = OrderedDict()
    od["a"] = 1
    od["b"] = 2
    od.move_to_end("a")
    print("OrderedDict:", od)


def demo_heap():
    heap = [3, 1, 4]
    heapify(heap)
    heappush(heap, 2)
    print("Heap:", heappop(heap))


def demo_binary_search():
    arr = [1, 3, 3, 5, 7]
    index = bisect.bisect_left(arr, 3)
    print("Binary Search Index:", index)


def demo_permutations_combinations():
    perm = list(permutations([1, 2, 3]))
    comb = list(combinations([1, 2, 3], 2))
    print("Permutations:", perm)
    print("Combinations:", comb)


def demo_cartesian_product():
    cartesian = list(product([1, 2], ["A", "B"]))
    print("Cartesian Product:", cartesian)


def demo_lru_cache():
    @lru_cache(None)
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    print("Fibonacci:", fib(10))


def demo_random():
    arr = [1, 2, 3, 4, 5]
    random.shuffle(arr)
    print("Shuffled Array:", arr)
    print("Random Integer:", random.randint(1, 10))


def demo_accumulate():
    # Basic accumulate (cumulative sum)
    nums = [1, 2, 3, 4, 5]
    cumulative_sum = list(accumulate(nums))
    print("Cumulative Sum:", cumulative_sum)  # [1, 3, 6, 10, 15]
    
    # Accumulate with custom function (product)
    cumulative_product = list(accumulate(nums, lambda x, y: x * y))
    print("Cumulative Product:", cumulative_product)  # [1, 2, 6, 24, 120]
    
    # Accumulate with max function
    data = [3, 1, 4, 1, 5, 9, 2]
    running_max = list(accumulate(data, max))
    print("Running Maximum:", running_max)  # [3, 3, 4, 4, 5, 9, 9]


def demo_math():
    print("Factorial:", factorial(5))
    print("GCD:", gcd(48, 18))
