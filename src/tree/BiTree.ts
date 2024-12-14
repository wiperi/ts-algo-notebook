import * as util from 'util';

export class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left ?? null;
    this.right = right ?? null;
  }
}

export class BiTree {
  root: TreeNode;
  nodes: TreeNode[] = [];

  constructor(template?: number[]) {
    template?.forEach((v, i) => (this.nodes[i] = new TreeNode(v)));

    this.nodes.forEach((v, i) => {
      const left = 2 * i + 1;
      const right = 2 * i + 2;

      if (left < template.length) v.left = this.nodes[left];
      if (right < template.length) v.right = this.nodes[right];
    });

    this.root = this.nodes[0] ?? null;
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
      if (!node) return;

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
