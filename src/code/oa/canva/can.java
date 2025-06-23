package code.oa.canva;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.TreeMap;

public class can {
    public static int findTotal(List<Integer> cans) {
        int res = 0;
        while (cans.size() > 0) {
            int mi = 0;
            int mn = cans.get(0);

            for (int i = 0;i < cans.size(); i++) {
                if (cans.get(i) < mn) {
                    mn = cans.get(i);
                    mi = i;
                }
            }

            cans.remove(mi);
            res += mn;

            if (mi < cans.size()) {
                cans.remove(mi);
            }
            if (mi - 1 >= 0) {
                cans.remove(mi - 1);
            }
        }

        return res;
    }

    public static int findTotalWeight(List<Integer> cans) {
        int res = 0;
        int n = cans.size();
        boolean[] vis = new boolean[n];

        while (true) {
            int mi = Integer.MAX_VALUE;
            int pos = -1;

            for (int i = 0; i < n; i++) {
                if (vis[i]) continue;
                if (cans.get(i) < mi) {
                    mi = cans.get(i);
                    pos = i;
                }
            }

            if (pos == -1) break;

            res += mi;
            vis[pos] = true;
            // 标记当前最小元素右边第一个未标记的
            for (int i = pos + 1; i < n; i++) {
                if (!vis[i]) {
                    vis[i] = true;
                    break;
                }
            }
            // 标记当前最小元素左边第一个未标记的
            for (int i = pos - 1; i >= 0; i--) {
                if (!vis[i]) {
                    vis[i] = true;
                    break;
                }
            }
        }

        return res;
    }


    public static void main(String[] args) {
        List<List<Integer>> testCases = new ArrayList<>();
        List<Integer> expected = new ArrayList<>();

        testCases.add(new ArrayList<>(Arrays.asList(5, 4, 1, 3, 2)));
        expected.add(3);

        testCases.add(new ArrayList<>(Arrays.asList(2, 2, 2, 2, 2)));
        expected.add(5);

        testCases.add(new ArrayList<>(Arrays.asList(9, 8, 7, 6, 5)));
        expected.add(6);

        testCases.add(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5)));
        expected.add(6);

        testCases.add(new ArrayList<>(Arrays.asList(7)));
        expected.add(7);

        testCases.add(new ArrayList<>(Arrays.asList()));
        expected.add(0);

        for (int i = 0; i < testCases.size(); i++) {
            List<Integer> cans = testCases.get(i);
            int result = findTotal(new ArrayList<>(cans)); // 传副本避免修改原数据
            if (result == expected.get(i)) {
                System.out.println("Test case " + (i + 1) + " passed.");
            } else {
                System.out.println("Test case " + (i + 1) + " failed: expected " + expected.get(i) + ", got " + result);
            }
        }

        for (int i = 0; i < testCases.size(); i++) {
            List<Integer> cans = testCases.get(i);
            int result = findTotalWeight(new ArrayList<>(cans)); // 传副本避免修改原数据
            if (result == expected.get(i)) {
                System.out.println("Test case " + (i + 1) + " passed.");
            } else {
                System.out.println("Test case " + (i + 1) + " failed: expected " + expected.get(i) + ", got " + result);
            }
        }
    }
}
