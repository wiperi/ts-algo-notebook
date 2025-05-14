
declare global {
  class TreeNode {
    val: any;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val?: any, left?: TreeNode | null, right?: TreeNode | null);
  }

  class ListNode<T = number> {
    val: T | null;
    next: ListNode<T> | null;
  
    constructor(val?: T, next?: ListNode<T> | null);
  }
}

export {};
