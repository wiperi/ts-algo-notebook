function knapsack(weights: number[], values: number[], capacity: number): number {
  const n = weights.length;

  // 状态：背包承重量，可选择物品
  // 选择：对于每个物品，装进背包还是不放进背包
  // dp[i][j] = 对于前i个item，承重量为j的背包，背包的最大价值
  const dp: number[][] = Array.from({ length: n + 1 }, () => Array(capacity + 1).fill(0));

  for (let i = 1; i <= n; i++) {
    for (let w = 0; w <= capacity; w++) {
      // weight of current item
      let weight = weights[i - 1];

      if (w < weight) {
        // Exclude the item
        dp[i][w] = dp[i - 1][w];
      } else {
        // Include the item or exclude it
        dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weight] + values[i - 1]);
      }
    }
  }

  return dp[n][capacity];
}

(function knapsackRecursive(weights: number[], values: number[], capacity: number): number {
  const n = weights.length;

  // Helper function for recursion
  function dp(i: number, capacity: number): number {
    // Base case: no items left or no remaining capacity
    if (i === 0 || capacity === 0) {
      return 0;
    }

    let weight = weights[i - 1];
    let value = values[i  - 1];

    // If the weight of the current item is more than the remaining capacity, skip it
    if (weight > capacity) {
      return dp(i - 1, capacity);
    }

    // Otherwise, consider including or excluding the current item
    const excludeItem = dp(i - 1, capacity);

    const includeItem = value + dp(i - 1, capacity - weight);

    return Math.max(excludeItem, includeItem);
  }

  return dp(n, capacity);
});

export {};
