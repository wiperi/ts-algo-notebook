package code.oa.canva;
import java.util.*;

public class FriendRecommender {
    public static List<Integer> getRecommendedFriends(int n, List<List<Integer>> friendships) {
        List<List<Integer>> e = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            e.add(new ArrayList<>());
        }

        for (List<Integer> x : friendships) {
            int u = x.get(0);
            int v = x.get(1);
            e.get(u).add(v);
            e.get(v).add(u);
        }

        int[] vis = new int[n];
        int[] cnt = new int[n];
        List<Integer> ans = new ArrayList<>(Collections.nCopies(n, -1));

        for (int i = 0; i < n; i++) {
            for (int j : e.get(i)) {
                vis[j] = 1;
                for (int k : e.get(j)) {
                    if (k != i && vis[k] == 0) {
                        cnt[k]++;
                    }
                }
            }

            int pos = -1;
            int mx = 0;
            for (int j = 0; j < n; j++) {
                if (j == i || vis[j] == 1) continue;
                if (cnt[j] > mx || (cnt[j] == mx && j < pos)) {
                    mx = cnt[j];
                    pos = j;
                }
            }

            ans.set(i, pos);

            for (int j : e.get(i)) vis[j] = 0;
            Arrays.fill(cnt, 0);
        }

        return ans;
    }

    // 用于运行测试
    public static void main(String[] args) {
        List<TestCase> testCases = Arrays.asList(
            new TestCase(4, Arrays.asList(Arrays.asList(0, 1), Arrays.asList(1, 2), Arrays.asList(2, 3)), Arrays.asList(2, 3, 0, 1)),
            new TestCase(3, Arrays.asList(Arrays.asList(0, 1), Arrays.asList(1, 2), Arrays.asList(0, 2)), Arrays.asList(-1, -1, -1)),
            new TestCase(4, Arrays.asList(Arrays.asList(0, 1), Arrays.asList(1, 2)), Arrays.asList(2, -1, 0, -1)),
            new TestCase(4, Arrays.asList(Arrays.asList(0, 1), Arrays.asList(1, 2), Arrays.asList(1, 3), Arrays.asList(0, 3), Arrays.asList(2, 3)), Arrays.asList(2, -1, 0, -1)),
            new TestCase(5, Arrays.asList(Arrays.asList(0, 1), Arrays.asList(1, 2), Arrays.asList(1, 3), Arrays.asList(2, 4), Arrays.asList(3, 4)), Arrays.asList(2, 4, 3, 2, 1)),
            new TestCase(5, Arrays.asList(Arrays.asList(0, 1), Arrays.asList(0, 2), Arrays.asList(1, 3), Arrays.asList(2, 3), Arrays.asList(3, 4)), Arrays.asList(3,2,1,0,1)),
            new TestCase(1, Collections.emptyList(), Arrays.asList(-1))
        );

        for (int i = 0; i < testCases.size(); i++) {
            TestCase tc = testCases.get(i);
            List<Integer> result = getRecommendedFriends(tc.n, tc.edges);
            if (result.equals(tc.expected)) {
                System.out.println("Test case " + (i + 1) + " passed.");
            } else {
                System.out.println("Test case " + (i + 1) + " failed.");
                System.out.println("Expected: " + tc.expected);
                System.out.println("Got     : " + result);
            }
        }
    }

    static class TestCase {
        int n;
        List<List<Integer>> edges;
        List<Integer> expected;

        TestCase(int n, List<List<Integer>> edges, List<Integer> expected) {
            this.n = n;
            this.edges = edges;
            this.expected = expected;
        }
    }
}
