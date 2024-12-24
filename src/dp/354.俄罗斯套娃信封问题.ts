/*
 * @lc app=leetcode.cn id=354 lang=typescript
 *
 * [354] 俄罗斯套娃信封问题
 */

import _ from 'lodash';

// @lc code=start
function maxEnvelopes(envelopes: number[][]): number {
  // let f(x) be how many times envelop x can russian doll
  // for input [a], f(a) = 1
  // for input [a, b,c, d]
  // f(a) = max(f(m) + 1, 1), m in [b,c,d] and m is larger than a

  envelopes.sort((a, b) => {
    return _.sum(a) - _.sum(b);
  });

  let dp = Array(envelopes.length).fill(1);

  for (let i = 0; i < envelopes.length; i++) {
    for (let j = 0; j < i; j++) {
      if (envelopes[j][0] >= envelopes[i][0]) continue;
      if (envelopes[j][1] >= envelopes[i][1]) continue;
      // now, envelopes[i] is larger then envelopes[j]
      dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }

  return _.max(dp);
}
// @lc code=end
