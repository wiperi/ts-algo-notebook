/*
 * @lc app=leetcode.cn id=1079 lang=typescript
 *
 * [1079] 活字印刷
 */

// @lc code=start
function numTilePossibilities(tiles: string): number {
  // 输入存在重复， so 排序并维护相同元素中间的相对顺序
  // 元素不可复用， so 使用used，记录使用情况
  // 顺序有关， so 每个节点的选择空间 for 循环从0开始

  // 选择：对于每个子集，可选择还未被选过的元素



  let used = new Set();
  let res = 0;

  // @ts-ignore
  tiles = tiles.split('').sort();
  backtrack();

  return res;
  
  function backtrack() {
    
    
    for (let i = 0; i < tiles.length; i++) {
      if (used.has(i)) continue;
      if (i > 0 && tiles[i] === tiles[i - 1] && used.has(i - 1) === false) continue;
      
      res++;
      used.add(i);
      backtrack()
      used.delete(i)
    }
  }
    
};
// @lc code=end

if (require.main === module) {
  console.log(numTilePossibilities('cdc'))
}

