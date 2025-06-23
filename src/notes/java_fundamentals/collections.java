package notes.java_fundamentals;

import java.util.*;

/**
 * 常见Java集合类的用法和算法题中的应用
 */
public class collections {
    
    public static void main(String[] args) {
        // 数组相关操作
        arrayOperations();
        
        // List相关操作
        listOperations();
        
        // Map相关操作
        mapOperations();
        
        // Set相关操作
        setOperations();
        
        // 队列和栈相关操作
        queueAndStackOperations();
        
        // 优先队列相关操作
        priorityQueueOperations();
    }
    
    /**
     * 数组相关操作
     */
    private static void arrayOperations() {
        int[] array = {5, 2, 9, 1, 5, 6};
        
        // 数组排序
        Arrays.sort(array);
        System.out.println("排序后的数组: " + Arrays.toString(array));
        
        // 二分查找（要求数组已排序）
        int index = Arrays.binarySearch(array, 5);
        System.out.println("元素5的索引: " + index);
        
        // 数组填充
        int[] newArray = new int[5];
        Arrays.fill(newArray, 10);
        System.out.println("填充后的数组: " + Arrays.toString(newArray));
        
        // 数组复制
        int[] copyArray = Arrays.copyOf(array, array.length);
        System.out.println("复制的数组: " + Arrays.toString(copyArray));
        
        // 数组部分复制
        int[] partialCopy = Arrays.copyOfRange(array, 1, 4);
        System.out.println("部分复制的数组: " + Arrays.toString(partialCopy));
    }
    
    /**
     * List相关操作
     */
    private static void listOperations() {
        List<Integer> list = new ArrayList<>();
        
        // 添加元素
        list.add(5);
        list.add(2);
        list.add(9);
        list.add(1);
        System.out.println("原始列表: " + list);
        
        // 在指定位置添加元素
        list.add(1, 7);
        System.out.println("添加元素后的列表: " + list);
        
        // 获取元素
        int element = list.get(2);
        System.out.println("索引2的元素: " + element);
        
        // 删除元素
        list.remove(0);
        System.out.println("删除元素后的列表: " + list);
        
        // 查找元素索引
        int index = list.indexOf(9);
        System.out.println("元素9的索引: " + index);
        
        // 列表排序
        Collections.sort(list);
        System.out.println("排序后的列表: " + list);
        
        // 列表反转
        Collections.reverse(list);
        System.out.println("反转后的列表: " + list);
        
        // 查找最大值和最小值
        int max = Collections.max(list);
        int min = Collections.min(list);
        System.out.println("最大值: " + max + ", 最小值: " + min);
        
        // 二分查找（要求列表已排序）
        Collections.sort(list);
        index = Collections.binarySearch(list, 7);
        System.out.println("元素7的索引: " + index);
        
        // 列表转数组
        Integer[] array = list.toArray(new Integer[0]);
        System.out.println("列表转数组: " + Arrays.toString(array));
        
        // 数组转列表
        List<Integer> arrayToList = Arrays.asList(1, 2, 3, 4, 5);
        System.out.println("数组转列表: " + arrayToList);
    }
    
    /**
     * Map相关操作
     */
    private static void mapOperations() {
        Map<String, Integer> map = new HashMap<>();
        
        // 添加键值对
        map.put("Alice", 25);
        map.put("Bob", 30);
        map.put("Charlie", 22);
        System.out.println("原始Map: " + map);
        
        // 获取值
        int age = map.get("Bob");
        System.out.println("Bob的年龄: " + age);
        
        // 检查键是否存在
        boolean containsKey = map.containsKey("David");
        System.out.println("是否包含David: " + containsKey);
        
        // 检查值是否存在
        boolean containsValue = map.containsValue(25);
        System.out.println("是否包含值25: " + containsValue);
        
        // 获取所有键
        Set<String> keys = map.keySet();
        System.out.println("所有键: " + keys);
        
        // 获取所有值
        Collection<Integer> values = map.values();
        System.out.println("所有值: " + values);
        
        // 遍历Map
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        // 使用getOrDefault
        int davidAge = map.getOrDefault("David", 0);
        System.out.println("David的年龄(默认值): " + davidAge);
        
        // 使用putIfAbsent
        map.putIfAbsent("Eve", 28);
        System.out.println("添加Eve后的Map: " + map);
        
        // 删除键值对
        map.remove("Charlie");
        System.out.println("删除Charlie后的Map: " + map);
    }
    
    /**
     * Set相关操作
     */
    private static void setOperations() {
        Set<Integer> set = new HashSet<>();
        
        // 添加元素 
        set.add(5);
        set.add(2);
        set.add(9);
        set.add(5); // 重复元素不会被添加
        System.out.println("HashSet: " + set);
        
        // 检查元素是否存在
        boolean contains = set.contains(2);
        System.out.println("是否包含2: " + contains);
        
        // 删除元素
        set.remove(2);
        System.out.println("删除2后的Set: " + set);
        
        // TreeSet - 有序集合
        Set<Integer> treeSet = new TreeSet<>();
        treeSet.add(5);
        treeSet.add(2);
        treeSet.add(9);
        System.out.println("TreeSet(自然排序): " + treeSet);
        
        // 集合操作
        Set<Integer> set1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        Set<Integer> set2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8));
        
        // 并集
        Set<Integer> union = new HashSet<>(set1);
        union.addAll(set2);
        System.out.println("并集: " + union);
        
        // 交集
        Set<Integer> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        System.out.println("交集: " + intersection);
        
        // 差集
        Set<Integer> difference = new HashSet<>(set1);
        difference.removeAll(set2);
        System.out.println("差集: " + difference);
    }
    
    /**
     * 队列和栈相关操作
     */
    private static void queueAndStackOperations() {
        // 队列
        Queue<Integer> queue = new LinkedList<>();
        
        // 添加元素
        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
        System.out.println("队列: " + queue);
        
        // 查看队首元素
        int head = queue.peek();
        System.out.println("队首元素: " + head);
        
        // 移除队首元素
        int removed = queue.poll();
        System.out.println("移除的元素: " + removed);
        System.out.println("移除后的队列: " + queue);
        
        // 栈（使用Deque实现）
        Deque<Integer> stack = new ArrayDeque<>();
        
        // 添加元素
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println("栈: " + stack);
        
        // 查看栈顶元素
        int top = stack.peek();
        System.out.println("栈顶元素: " + top);
        
        // 弹出栈顶元素
        int poped = stack.pop();
        System.out.println("弹出的元素: " + poped);
        System.out.println("弹出后的栈: " + stack);
    }
    
    /**
     * 优先队列相关操作
     */
    private static void priorityQueueOperations() {
        // 默认是小顶堆
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.offer(5);
        minHeap.offer(2);
        minHeap.offer(9);
        minHeap.offer(1);
        
        System.out.println("小顶堆: " + minHeap);
        System.out.println("堆顶元素: " + minHeap.peek());
        
        // 逐个取出元素（会按照优先级顺序）
        System.out.print("按优先级顺序取出元素: ");
        while (!minHeap.isEmpty()) {
            System.out.print(minHeap.poll() + " ");
        }
        System.out.println();
        
        // 大顶堆
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.offer(5);
        maxHeap.offer(2);
        maxHeap.offer(9);
        maxHeap.offer(1);
        
        System.out.println("大顶堆: " + maxHeap);
        System.out.println("堆顶元素: " + maxHeap.peek());
        
        // 自定义比较器
        PriorityQueue<String> customQueue = new PriorityQueue<>(
            Comparator.comparing(String::length).thenComparing(String::compareTo)
        );
        customQueue.offer("apple");
        customQueue.offer("banana");
        customQueue.offer("pear");
        customQueue.offer("kiwi");
        
        System.out.println("自定义优先队列: " + customQueue);
    }
}
