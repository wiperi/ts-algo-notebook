# Generator and Comprehension Examples
def demo_generators_and_comprehensions():
    # Create a generator expression
    gen = (i for i in range(5))

    # Check its type
    print(type(gen))  # <class 'generator'>

    # Compare with similar constructs
    list_comp = [i for i in range(5)]  # List comprehension
    set_comp = {i for i in range(5)}  # Set comprehension
    dict_comp = {i: i * i for i in range(5)}  # Dict comprehension

    print(type(list_comp))  # <class 'list'>
    print(type(set_comp))  # <class 'set'>
    print(type(dict_comp))  # <class 'dict'>

    # Using the generator
    for i in gen:
        print(i)  # Prints: 0, 1, 2, 3, 4

    # Note: generator can only be used once
    print(list(gen))  # [] (empty because generator is already exhausted)


# Built-in Iterator Functions
def demo_builtin_iterators():
    print("\nBuilt-in functions that return iterators:")

    # 0. iter() - creates an iterator from an iterable
    my_iter = iter([1, 2, 3])
    print(f"iter: {type(my_iter)}")
    print(f"next value: {next(my_iter)}")  # 1
    print(f"next value: {next(my_iter)}")  # 2
    print(f"remaining values: {list(my_iter)}")  # [3]

    # 1. range() - returns a range iterator
    range_iter = range(3)
    print(f"range: {type(range_iter)}, values: {list(range_iter)}")

    # 2. map() - returns a map iterator
    map_iter = map(lambda x: x * 2, [1, 2, 3])
    print(f"map: {type(map_iter)}, values: {list(map_iter)}")

    # 3. filter() - returns a filter iterator
    filter_iter = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    print(f"filter: {type(filter_iter)}, values: {list(filter_iter)}")

    # 4. zip() - returns a zip iterator
    zip_iter = zip([1, 2], ["a", "b"])
    print(f"zip: {type(zip_iter)}, values: {list(zip_iter)}")

    # 5. enumerate() - returns an enumerate iterator
    enum_iter = enumerate(["a", "b", "c"])
    print(f"enumerate: {type(enum_iter)}, values: {list(enum_iter)}")

    # 6. reversed() - returns a reverse iterator
    rev_iter = reversed([1, 2, 3])
    print(f"reversed: {type(rev_iter)}, values: {list(rev_iter)}")


# Itertools Module Examples
def demo_itertools():
    from itertools import permutations, combinations, product

    print("\nItertools functions:")

    # Permutations
    perm_iter = permutations([1, 2, 3], 2)
    print(f"permutations: {type(perm_iter)}, values: {list(perm_iter)}")

    # Combinations
    comb_iter = combinations([1, 2, 3], 2)
    print(f"combinations: {type(comb_iter)}, values: {list(comb_iter)}")

    # Product
    prod_iter = product([1, 2], ["a", "b"])
    print(f"product: {type(prod_iter)}, values: {list(prod_iter)}")
