/*
 * @lc app=leetcode.cn id=763 lang=typescript
 *
 * [763] 划分字母区间
 */

import _ from "lodash";

// @lc code=start
function partitionLabels(s: string): number[] {

  // 每个字符的最后出现位置
  let lastIndex: Record<string, number> = {};
  for (let i = 0; i < s.length; i++) {
    lastIndex[s[i]] = i;
  }

  const res = [];
  let start = 0
  let end = 0;
  for (let i of _.range(s.length)) {
    end = Math.max(end, lastIndex[s[i]]);

    if (i === end) {
      res.push(end - start + 1);
      start = end + 1;
    }
  }

  return res;
}

// @lc code=end

(function partitionLabels(s: string): number[] {
  // for a, find first , last a, they must in a partition 
  // a map record all used char, if new one in map, then it is not a new partition

  // char to indexOfPartition
  let map = new Map();

  /**
   * for i in s:
   * 
   * if (i not used): new partition from first i to last i 
   * if (i used): add to partition
   */

  let partition: string[][] = [];
  let str = s.split('');

  for (let i = 0; i < str.length; i++) {

    let char = str[i];

    if (map.has(char) === false) {
      partition.push([]);
      
      let pIndex = partition.length - 1;
      
      let start = i;
      let end = str.lastIndexOf(char);

      for (let j = start; j <= end; j++) {
        end = Math.max(end, str.lastIndexOf(str[j]));
        map.set(str[j], pIndex);
        partition[pIndex].push(str[j]);
      }

      i = end;
    } else {
      // char used
      let pIndex = map.get(char);
      partition[pIndex].push(char);
    }
  }

  // console.log(partition)
  return partition.map(p => p.length);
})
