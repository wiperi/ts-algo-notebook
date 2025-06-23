package code.oa.canva;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class swap {
    List<Integer> arr;
    Map<Integer, Long> mp = new HashMap<>();

    public long getMax(List<Integer> arr) {
        this.arr = arr;
        return f(0);
    }

    long f(int i) {
        if (this.mp.containsKey(i)) {
            return this.mp.get(i);
        }

        if (i >= this.arr.size()) {
            return 0;
        } else if (i == this.arr.size() - 1) {
            return this.arr.get(i) * (i + 1);
        }

        long r1 = f(i + 1) + this.arr.get(i) * (i + 1);

        long v1 = this.arr.get(i);
        long v2 = this.arr.get(i + 1);
        long noSwap = v1 * (i + 1) + v2 * (i + 2);
        long swap = v1 * (i + 2) + v2 * (i + 1);
        long r2 = f(i + 2) + Math.max(swap, noSwap);

        this.mp.put(i, Math.max(r1, r2));
        return this.mp.get(i);
    }

    public long getMaximumSumOfStrengths( List<Integer> arr) {
        int n = arr.size();
        long[] f = new long[n];
        f[0] = arr.get(0);
        if (n == 1) return f[0];
        f[1] = Math.max(f[0] + (long)2 * arr.get(1), arr.get(1) + (long)2 * arr.get(0));
        for (int i = 2; i < n; i++) {
            f[i] = f[i - 1] + ((long)(i + 1)) * arr.get(i);
            f[i] = Math.max(f[i], f[i - 2] + (long)i * arr.get(i) + ((long)(i + 1)) * arr.get(i - 1));
        }
        return f[n - 1];
    }

    public static void main(String[] args) {

        // 原测试用例
        System.out.println(new swap().getMax(List.of(1, 9, 7, 3, 2))); 

        // 新增测试用例1：数组元素全为升序
        System.out.println(new swap().getMax(List.of(1, 2, 3, 4, 5))); 

        // 新增测试用例2：数组元素全为降序
        System.out.println(new swap().getMax(List.of(5, 4, 3, 2, 1))); 

        // 新增测试用例3：包含重复元素
        System.out.println(new swap().getMax(List.of(1, 2, 2, 3, 3))); 

        // 新增测试用例4：只有一个元素的数组
        System.out.println(new swap().getMax(List.of(5))); 

        // 新增测试用例5：元素为负数的数组
        System.out.println(new swap().getMax(List.of(-1, -2, -3))); 
        
        // 原测试用例
        System.out.println(new swap().getMaximumSumOfStrengths(List.of(1, 9, 7, 3, 2))); 

        // 新增测试用例1：数组元素全为升序
        System.out.println(new swap().getMaximumSumOfStrengths(List.of(1, 2, 3, 4, 5))); 

        // 新增测试用例2：数组元素全为降序
        System.out.println(new swap().getMaximumSumOfStrengths(List.of(5, 4, 3, 2, 1))); 

        // 新增测试用例3：包含重复元素
        System.out.println(new swap().getMaximumSumOfStrengths(List.of(1, 2, 2, 3, 3))); 

        // 新增测试用例4：只有一个元素的数组
        System.out.println(new swap().getMaximumSumOfStrengths(List.of(5))); 

        // 新增测试用例5：元素为负数的数组
        System.out.println(new swap().getMaximumSumOfStrengths(List.of(-1, -2, -3))); 
    }
}