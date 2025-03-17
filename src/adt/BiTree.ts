import * as util from 'util';

export class TreeNode {
  val: any;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val?: any, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val;
    this.left = left ?? null;
    this.right = right ?? null;
  }
}

export class BiTree {
  root: TreeNode;
  nodes: TreeNode[] = [];

  constructor(iterable?: any[]) {
    if (iterable === undefined || iterable.length === 0) {
      this.root = new TreeNode();
      this.nodes[0] = this.root;
      return;
    }

    iterable.forEach((v, i) => {
      if (v === null) {
        this.nodes[i] = null;
      } else {
        this.nodes[i] = new TreeNode(v)
      }
    });

    this.nodes.forEach((v, i) => {
      if (v === null) return;

      const left = 2 * i + 1;
      const right = 2 * i + 2;

      if (left < iterable.length) v.left = this.nodes[left];
      if (right < iterable.length) v.right = this.nodes[right];
    });

    this.root = this.nodes[0];
  }

  // Change console.log behavior
  [util.inspect.custom]() {
    return BiTree.printTree(this.root);
  }

  static printTree(root: TreeNode | null): string {
    let res = '';
    if (!root) {
      res = 'null';
      return res;
    }

    printNode(root);
    return res;

    // 递归遍历树，按层级打印
    function printNode(node: TreeNode | null, indent: string = ''): void {
      if (node === null) return;

      // 先打印右子树
      if (node.right) {
        printNode(node.right, indent + '    ');
      }

      // 打印当前节点
      res += indent + node.val + '\n';

      // 然后打印左子树
      if (node.left) {
        printNode(node.left, indent + '    ');
      }
    }
  }
}

if (require.main === module) {
  const tree = new BiTree(Array.from({ length: 7 }, (_, i) => i + 1));
  console.log(tree);
}
