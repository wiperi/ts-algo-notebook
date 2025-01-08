class TreeNode<T> {
  value: T;
  left: TreeNode<T> | null = null;
  right: TreeNode<T> | null = null;

  constructor(value: T) {
    this.value = value;
  }
}

export class BinarySearchTree<T> {
  private root: TreeNode<T> | null = null;

  constructor(iterable?: Iterable<T>) {
    if (iterable) {
      for (const value of iterable) {
        this.insert(value);
      }
    }
  }

  // 插入节点
  insert(value: T): void {
    const newNode = new TreeNode(value);
    if (this.root === null) {
      this.root = newNode;
    } else {
      this.insertNode(this.root, newNode);
    }
  }
  private insertNode(node: TreeNode<T>, newNode: TreeNode<T>): void {
    if (newNode.value < node.value) {
      if (node.left === null) {
        node.left = newNode;
      } else {
        this.insertNode(node.left, newNode);
      }
    } else {
      if (node.right === null) {
        node.right = newNode;
      } else {
        this.insertNode(node.right, newNode);
      }
    }
  }


  // 查找节点
  find(value: T): TreeNode<T> | null {
    return this.findNode(this.root, value);
  }

  private findNode(node: TreeNode<T> | null, value: T): TreeNode<T> | null {
    if (node === null) return null;

    if (value === node.value) {
      return node;
    } else if (value < node.value) {
      return this.findNode(node.left, value);
    } else {
      return this.findNode(node.right, value);
    }
  }

  // 删除节点
  delete(value: T): void {
    this.root = this.deleteNode(this.root, value);
  }

  private deleteNode(node: TreeNode<T> | null, value: T): TreeNode<T> | null {
    if (node === null) return null;

    if (value < node.value) {
      node.left = this.deleteNode(node.left, value);
    } else if (value > node.value) {
      node.right = this.deleteNode(node.right, value);
    } else {
      if (node.left !== null && node.right !== null) {
        const minRight = this.findMinNode(node.right);
        node.value = minRight!.value;
        node.right = this.deleteNode(node.right, minRight!.value);
      } else {
        node = node.left || node.right;
      }
    }
    return node;
  }

  private findMinNode(node: TreeNode<T>): TreeNode<T> {
    while (node.left !== null) {
      node = node.left;
    }
    return node;
  }

  // 中序遍历
  inOrderTraversal(callback: (value: T) => void): void {
    this.inOrder(this.root, callback);
  }

  private inOrder(node: TreeNode<T> | null, callback: (value: T) => void): void {
    if (node !== null) {
      this.inOrder(node.left, callback);
      callback(node.value);
      this.inOrder(node.right, callback);
    }
  }

  // 从数组构建 BST
  static fromArray<T>(arr: T[]): BinarySearchTree<T> {
    const bst = new BinarySearchTree<T>();
    for (const value of arr) {
      bst.insert(value);
    }
    return bst;
  }

  // 检查是否为合法的 BST
  static isBST<T>(node: TreeNode<T> | null, min: T | null = null, max: T | null = null): boolean {
    if (node === null) return true;

    if ((min !== null && node.value <= min) || (max !== null && node.value >= max)) {
      return false;
    }

    return this.isBST(node.left, min, node.value) && this.isBST(node.right, node.value, max);
  }
}
