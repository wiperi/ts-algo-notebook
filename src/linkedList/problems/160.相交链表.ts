/*
 * @lc app=leetcode.cn id=160 lang=typescript
 *
 * [160] 相交链表
 */

import { ListNode } from "@/linkedList/LinkedList";

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

function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
  let visited = new Set();

  let p = headA;
  while (p !== null) {
    visited.add(p)
    p = p.next
  }

  p = headB;
  while (p !== null) {
    if (visited.has(p)) return p;
    
    p = p.next
  }

  return null;
};
// @lc code=end


export {}