/*
 * @lc app=leetcode.cn id=139 lang=typescript
 *
 * [139] 单词拆分
 */

namespace Iter {
  // @lc code=start
  function wordBreak(s: string, wordDict: string[]): boolean {
    let wordSet = new Set(wordDict);

    // dp[i] = (dp[j] is true) && s[j, i] is in the dict
    let dp = Array(s.length + 1).fill(false);
    dp[0] = true;

    for (let i = 1; i <= s.length; i++) {
      for (let j = 0; j < i; j++) {
        if (dp[j] && wordSet.has(s.substring(j, i))) {
          dp[i] = true;
          break;
        }
      }
    }

    return dp[s.length];
  }
  // @lc code=end
}

namespace Recur {
  function wordBreak(s: string, wordDict: string[]): boolean {
    // f(s) = f(s - word) || f(s - word2) || ...

    return dp(0);

    function dp(start: number) {
      if (start === s.length) {
        return true;
      }

      let res = false;
      for (let word of wordDict) {
        if (s.slice(start, start + word.length) != word) {
          continue;
        }
        res = res || dp(start + word.length);
      }

      return res;
    }
  }
}

namespace MemoRecur {
  function wordBreak(s: string, wordDict: string[]): boolean {
    let memo = Array(s.length + 1).fill(null);

    return dp(0);

    function dp(start: number) {
      if (memo[start] !== null) {
        return memo[start];
      }

      if (start === s.length) {
        return true;
      }

      let res = false;
      for (let word of wordDict) {
        if (s.slice(start, start + word.length) != word) {
          continue;
        }
        res = res || dp(start + word.length);
      }

      memo[start] = res;
      return res;
    }
  }
}

namespace BackTrack {
  // lc code=start
  function wordBreak(s: string, wordDict: string[]): boolean {
    // state: how many char has already been matched
    // choice: match which word in the wordDict

    let res = false;

    backtrack(0);

    return res;

    function backtrack(start: number) {
      if (start === s.length) {
        res = true;
        return;
      }

      for (let word of wordDict) {
        if (s.substring(start).indexOf(word) !== 0) continue;

        backtrack(start + word.length);
        if (res === true) return;
      }
    }
  }
  // lc code=end
}

export {};
