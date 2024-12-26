/*
 * @lc app=leetcode.cn id=2 lang=typescript
 *
 * [2] 两数相加
 */

import { List, ListNode } from '@/list/List';

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  let dummy = new ListNode();

  let p = dummy;
  let carry = 0;

  // 开始执行加法，两条链表走完且没有进位时才能结束循环
  while (l1 || l2 || carry !== 0) {
        // 先加上上次的进位
        let val = carry;
        if (l1 !== null) {
            val += l1.val;
            l1 = l1.next;
        }
        if (l2 !== null) {
            val += l2.val;
            l2 = l2.next;
        }
        // 处理进位情况
        carry = Math.floor(val / 10);
        val = val % 10;
        // 构建新节点
        p.next = new ListNode(val);
        p = p.next;
  }

  return dummy.next;
}
// @lc code=end

if (require.main === module) {
  let res = addTwoNumbers(new List([1, 8, 6]).head, new List([1, 2, 3]).head);
  while (res) {
    console.log(res.val);
    res = res.next
  }
}
