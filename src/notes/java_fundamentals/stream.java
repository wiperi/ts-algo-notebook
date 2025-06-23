package notes.java_fundamentals;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Java Stream API的常见用法及在算法题中的应用
 */
public class stream {
    
    public static void main(String[] args) {
        // 创建Stream的几种方式
        createStreamExamples();
        
        // 常见的Stream操作
        commonStreamOperations();
        
        // 在算法题中的应用
        algorithmicApplications();
    }
    
    /**
     * 创建Stream的几种方式
     */
    private static void createStreamExamples() {
        System.out.println("===== 创建Stream示例 =====");
        
        // 1. 从集合创建
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
        Stream<Integer> streamFromCollection = list.stream();
        System.out.println("从集合创建: " + streamFromCollection.collect(Collectors.toList()));
        
        // 2. 从数组创建
        Integer[] array = {1, 2, 3, 4, 5};
        Stream<Integer> streamFromArray = Arrays.stream(array);
        System.out.println("从数组创建: " + streamFromArray.collect(Collectors.toList()));
        
        // 3. 基本类型数组
        int[] intArray = {1, 2, 3, 4, 5};
        IntStream intStream = Arrays.stream(intArray);
        System.out.println("从int数组创建: " + intStream.boxed().collect(Collectors.toList()));
        
        // 4. Stream.of方法
        Stream<Integer> streamOf = Stream.of(1, 2, 3, 4, 5);
        System.out.println("使用Stream.of创建: " + streamOf.collect(Collectors.toList()));
        
        // 5. 生成无限流
        Stream<Integer> infiniteStream = Stream.iterate(0, n -> n + 2).limit(5);
        System.out.println("使用iterate创建无限流: " + infiniteStream.collect(Collectors.toList()));
        
        // 6. 使用generate创建
        Stream<Double> randomStream = Stream.generate(Math::random).limit(5);
        System.out.println("使用generate创建: " + randomStream.collect(Collectors.toList()));
    }
    
    /**
     * 常见的Stream操作
     */
    private static void commonStreamOperations() {
        System.out.println("\n===== 常见Stream操作 =====");
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10);
        
        // 过滤
        List<Integer> filtered = numbers.stream()
                .filter(n -> n % 2 == 0)
                .collect(Collectors.toList());
        System.out.println("过滤偶数: " + filtered);
        
        // 映射
        List<Integer> mapped = numbers.stream()
                .map(n -> n * n)
                .collect(Collectors.toList());
        System.out.println("映射(平方): " + mapped);
        
        // 扁平化映射
        List<List<Integer>> nestedList = Arrays.asList(
                Arrays.asList(1, 2, 3),
                Arrays.asList(4, 5, 6),
                Arrays.asList(7, 8, 9)
        );
        List<Integer> flattened = nestedList.stream()
                .flatMap(Collection::stream)
                .collect(Collectors.toList());
        System.out.println("扁平化映射: " + flattened);
        
        // 排序
        List<Integer> sorted = numbers.stream()
                .sorted()
                .collect(Collectors.toList());
        System.out.println("自然排序: " + sorted);
        
        // 反向排序
        List<Integer> reverseSorted = numbers.stream()
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.toList());
        System.out.println("反向排序: " + reverseSorted);
        
        // 去重
        List<Integer> distinct = numbers.stream()
                .distinct()
                .collect(Collectors.toList());
        System.out.println("去重: " + distinct);
        
        // 限制元素数量
        List<Integer> limited = numbers.stream()
                .limit(5)
                .collect(Collectors.toList());
        System.out.println("限制前5个: " + limited);
        
        // 跳过元素
        List<Integer> skipped = numbers.stream()
                .skip(5)
                .collect(Collectors.toList());
        System.out.println("跳过前5个: " + skipped);
        
        // 查找和匹配
        boolean anyMatch = numbers.stream().anyMatch(n -> n > 8);
        boolean allMatch = numbers.stream().allMatch(n -> n > 0);
        boolean noneMatch = numbers.stream().noneMatch(n -> n < 0);
        Optional<Integer> firstElement = numbers.stream().findFirst();
        
        System.out.println("是否有大于8的元素: " + anyMatch);
        System.out.println("是否所有元素都大于0: " + allMatch);
        System.out.println("是否没有小于0的元素: " + noneMatch);
        System.out.println("第一个元素: " + firstElement.orElse(0));
        
        // 归约操作
        int sum = numbers.stream().reduce(0, Integer::sum);
        int max = numbers.stream().reduce(Integer.MIN_VALUE, Integer::max);
        int product = numbers.stream().reduce(1, (a, b) -> a * b);
        
        System.out.println("总和: " + sum);
        System.out.println("最大值: " + max);
        System.out.println("所有元素的乘积: " + product);
        
        // 收集器
        String joined = numbers.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(", "));
        System.out.println("连接成字符串: " + joined);
        
        // 分组
        Map<Boolean, List<Integer>> partitioned = numbers.stream()
                .collect(Collectors.partitioningBy(n -> n % 2 == 0));
        System.out.println("按奇偶分组: " + partitioned);
        
        // 统计
        IntSummaryStatistics stats = numbers.stream()
                .mapToInt(Integer::intValue)
                .summaryStatistics();
        System.out.println("统计: " + stats);
    }
    
    /**
     * Stream在算法题中的应用
     */
    private static void algorithmicApplications() {
        System.out.println("\n===== Stream在算法题中的应用 =====");
        
        // 1. 数组求和问题
        int[] nums = {1, 2, 3, 4, 5};
        int sum = Arrays.stream(nums).sum();
        System.out.println("数组求和: " + sum);
        
        // 2. 找出最大/最小值
        int max = Arrays.stream(nums).max().orElse(0);
        int min = Arrays.stream(nums).min().orElse(0);
        System.out.println("最大值: " + max + ", 最小值: " + min);
        
        // 3. 字符串数组分组(字母异位词分组)
        String[] words = {"eat", "tea", "tan", "ate", "nat", "bat"};
        Map<String, List<String>> anagrams = Arrays.stream(words)
                .collect(Collectors.groupingBy(word -> {
                    char[] chars = word.toCharArray();
                    Arrays.sort(chars);
                    return new String(chars);
                }));
        System.out.println("字母异位词分组: " + anagrams);
        
        // 4. 计数问题
        int[] arr = {1, 1, 2, 3, 3, 3, 4, 5, 5};
        Map<Integer, Long> countMap = Arrays.stream(arr)
                .boxed()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        System.out.println("元素计数: " + countMap);
        
        // 5. 数组转换问题
        int[] transformed = Arrays.stream(nums)
                .map(x -> x * x)
                .toArray();
        System.out.println("数组平方: " + Arrays.toString(transformed));
        
        // 6. 过滤问题
        int[] filtered = Arrays.stream(nums)
                .filter(x -> x % 2 == 0)
                .toArray();
        System.out.println("过滤偶数: " + Arrays.toString(filtered));
        
        // 7. 连续数字问题
        int[] sequence = {100, 4, 200, 1, 3, 2};
        Set<Integer> numSet = Arrays.stream(sequence).boxed().collect(Collectors.toSet());
        int longestStreak = 0;
        
        for (int num : numSet) {
            // 只检查序列的起点
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;
                
                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }
                
                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }
        System.out.println("最长连续序列长度: " + longestStreak);
    }
}
