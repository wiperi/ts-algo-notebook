/*
 * @lc app=leetcode.cn id=1593 lang=typescript
 *
 * [1593] 拆分字符串使唯一子字符串的数目最大
 */

// @lc code=start
function maxUniqueSplit(s: string): number {
  // 状态：正在决定第几个子串，已经分配了哪些字符
  // 选择：每个子串都可以包含任意长度的字符


  let set = new Set();
  let res = 0;
  
  backtrack(0);

  return res;

  function backtrack(start) {

    if (start === s.length) {
      res = Math.max(res, set.size);
      return;
    }
    
    for (let end = start +  1; end <= s.length; end++) {
      let sub = s.substring(start, end);
      
      if (set.has(sub)) continue;
      
      set.add(sub)
      backtrack(end);
      set.delete(sub);
    }
  }
};
// @lc code=end

if (require.main === module) {
  maxUniqueSplit("ababccc")
}

export {}
