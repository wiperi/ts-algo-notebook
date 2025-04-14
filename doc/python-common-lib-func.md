在算法练习中，Python 提供了丰富的内置 **库函数** 和 **数据结构模块**，这些工具大大简化了算法实现。以下是常见的库函数和数据结构总结，按功能分类。

---

## **1. 常见数据结构模块**

| **数据结构**                | **Python 内置模块/类**                | **功能及常用方法**                                   | **示例**                                $$            |
|-----------------------------|--------------------------------------|----------------------------------------------------|-----------------------------------------------------|
| **列表（List）**             | `list`                               | 动态数组，支持切片、添加、删除、排序等               | `my_list.append(1)`，`my_list.sort()`                |
| **元组（Tuple）**            | `tuple`                              | 不可变序列，支持存储多类型数据                       | `my_tuple = (1, 2, 3)`                              |
| **字典（Dict）**             | `dict`                               | 键值对映射，支持高效查找、插入、删除                 | `my_dict['key'] = 42`                               |
| **集合（Set）**              | `set`、`frozenset`                   | 集合运算（并、交、差集等）                           | `set1 & set2`，`set1.union(set2)`                    |
| **双端队列（Deque）**        | `collections.deque`                  | O(1) 时间复杂度的双端插入、删除                      | `q.appendleft(x)`，`q.pop()`                        |
| **计数器（Counter）**        | `collections.Counter`                | 统计元素频次                                        | `Counter(['a', 'b', 'a']).most_common(1)`            |
| **默认字典（Defaultdict）**  | `collections.defaultdict`            | 提供默认值的字典，避免键错误                         | `d = defaultdict(int)`，`d[key] += 1`                |
| **有序字典（OrderedDict）**  | `collections.OrderedDict`            | 按插入顺序维护键值对                                | `od.move_to_end('key')`                              |
| **优先队列（最小堆）**       | `heapq`                              | 最小堆实现，支持堆排序、优先队列                     | `heapq.heappop(heap)`                               |
| **固定大小数组（Array）**    | `array`                              | 轻量级、固定类型数组，节省内存                       | `arr = array('i', [1, 2, 3])`                       |
| **链表（手动实现）**         | 自行实现                             | 手动实现单链表、双链表                              | 无内置类，适合练习数据结构                           |
| **位集合（BitSet 类似）**    | `bitarray`（需安装）或位运算          | 位运算、布尔状态存储                                | `bitarray('1101')`                                  |

---

## **2. 常用算法模块与库**

| **算法功能**                | **Python 内置模块/函数**              | **功能及常用方法**                                 | **示例**                                            |
|-----------------------------|--------------------------------------|--------------------------------------------------|-----------------------------------------------------|
| **排序（Sorting）**          | `sorted()`、`list.sort()`             | 快速排序、稳定排序，支持按键排序                   | `sorted(arr, key=lambda x: x[1])`                    |
| **二分查找（Binary Search）**| `bisect`                             | 二分插入、查找，适用于有序列表                     | `bisect.bisect_left(arr, target)`                    |
| **堆排序、最小堆/最大堆**    | `heapq`                              | 最小堆实现、`heapify()`、`heappop()`                | `heapq.nlargest(3, arr)`                             |
| **全排列、组合生成**         | `itertools`                          | 全排列、组合、笛卡尔积                             | `itertools.permutations([1, 2, 3])`                  |
| **数学计算**                 | `math`、`cmath`                       | 阶乘、最大公约数、排列组合、浮点数、复数运算        | `math.gcd(a, b)`，`math.factorial(n)`                |
| **随机数生成**               | `random`                             | 生成随机数、打乱数组顺序、随机采样                  | `random.shuffle(arr)`，`random.randint(1, 10)`       |
| **动态规划缓存**             | `functools.lru_cache`                | 缓存函数返回值，适合递归优化                       | `@lru_cache(None)`                                  |
| **优先队列（多任务调度）**   | `queue.PriorityQueue`                | 用于任务优先级调度                                 | `q.put((priority, task))`                            |

---

## **3. Python 库函数与常见算法模块功能分析**

### **(1) `collections` 模块**  
专为处理复杂数据结构而设计，提供更高级的容器：
- **`deque`**：双端队列（常用于滑动窗口、BFS）。
- **`Counter`**：计数器（常用于统计字符、频次问题）。
- **`defaultdict`**：默认字典（避免 KeyError，常用于图算法的邻接表存储）。
- **`OrderedDict`**：有序字典，按插入顺序存储键值对。
  
**示例：**
```python
from collections import deque, Counter, defaultdict

# 1. 双端队列
dq = deque([1, 2, 3])
dq.appendleft(0)  # 左侧插入 O(1)
dq.pop()          # 右侧删除 O(1)

# 2. 计数器
cnt = Counter("abacaba")
print(cnt.most_common(1))  # 输出 [('a', 4)]

# 3. 默认字典
graph = defaultdict(list)
graph[0].append(1)
```

---

### **(2) `heapq` 模块**（最小堆实现优先队列）  
提供堆排序、优先队列支持，适合求**K 大/最小元素**、最短路径问题。
- **常用方法：** `heappush()`, `heappop()`, `heapify()`。

**示例：**
```python
import heapq

arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)               # 转换为最小堆 O(n)
smallest = heapq.heappop(arr)    # 弹出最小值 O(log n)
largest_k = heapq.nlargest(3, arr)
```

---

### **(3) `itertools` 模块**（排列、组合、生成器）  
适合解决排列组合问题，常见于回溯问题中的枚举、生成。

- **常用方法：**
  - **全排列**：`itertools.permutations(iterable, r)`。
  - **组合**：`itertools.combinations(iterable, r)`。
  - **笛卡尔积**：`itertools.product(iterable1, iterable2)`。

**示例：**
```python
from itertools import permutations, combinations, product

perm = list(permutations([1, 2, 3]))
comb = list(combinations([1, 2, 3], 2))
cartesian = list(product([1, 2], ['A', 'B']))
```

---

### **(4) `bisect` 模块**（二分查找）  
用于在有序列表中查找插入点，适合**插入、区间查找问题**。

- **常用方法：**
  - `bisect.bisect_left(arr, x)`：在数组中查找 `x` 左侧插入位置。
  - `bisect.bisect_right(arr, x)`：在数组中查找 `x` 右侧插入位置。

**示例：**
```python
import bisect

arr = [1, 3, 3, 5, 7]
index = bisect.bisect_left(arr, 3)  # 输出 1（插入到第 1 个位置前）
```

---

### **(5) `functools.lru_cache`**（递归优化、缓存）  
适合用于递归问题，如斐波那契数列、动态规划。  
- 通过缓存函数的返回值来避免重复计算，从而优化性能。

**示例：**
```python
from functools import lru_cache

@lru_cache(None)  # 无限制缓存大小
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(100))  # 快速计算第 100 项斐波那契数
```

---

## **总结：Python 常见库函数、数据结构适用场景**

| **功能/算法类型**         | **常用模块/类**            | **适用场景**                                 |
|---------------------------|---------------------------|----------------------------------------------|
| **数组、列表、排序**      | `list`、`sorted()`        | 快速排序、K 大/最小问题                      |
| **堆、优先队列**         | `heapq`                   | 堆排序、最短路径、K 大/最小元素查找         |
| **二分查找**             | `bisect`                  | 查找插入点、处理有序数组                    |
| **计数器、频次统计**     | `collections.Counter`     | 统计字符、元素频次                          |
| **图的邻接表存储**       | `collections.defaultdict` | 图搜索、BFS、DFS                            |
| **滑动窗口、队列**       | `collections.deque`       | 滑动窗口、队列操作                          |
| **动态规划递归优化**     | `functools.lru_cache`     | 斐波那契数列、递归 DP 问题                  |
| **排列组合生成**         | `itertools`               | 全排列、组合、笛卡尔积                       |

这些库函数极大提高了 Python 在算法练习中的开发效率，尤其适合快速实现复杂算法逻辑。