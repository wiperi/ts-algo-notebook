/*
 * @lc app=leetcode.cn id=1593 lang=typescript
 *
 * [1593] 拆分字符串使唯一子字符串的数目最大
 */

// @lc code=start
function maxUniqueSplit(s: string): number {
  // 状态：在决定第i个字符该不该拆分
  // 选择：拆分 / 不拆分

  // 被拆分的子串
  let set = new Set();
  let res = 0;

  backtrack(0, 1);

  return res;
  
  // start：闭区间
  // end：开区间
  function backtrack(start, end) {

    if (end === s.length + 1) {
      res = Math.max(res, set.size);
      return;
    } 

    // 不拆分当前字符（当前字符并入当前子串）
    backtrack(start, end + 1);

    // 拆分当前字符（记录并分割当前子串）
    let sub = s.substring(start, end);
    if (set.has(sub) === false) {
      set.add(sub);

      backtrack(end, end + 1);

      set.delete(sub);
    }    
  }
};
// @lc code=end

if (require.main === module) {
  maxUniqueSplit("ababccc")
}

export {}