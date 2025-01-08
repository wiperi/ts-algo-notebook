import { BiTree, TreeNode } from './BiTree';
import { __Node } from './MultiTree';

class Tree {
  static levelOrder(root: TreeNode): any[] {
    const res = [];

    const q = [root];

    while (q.length !== 0) {
      const levelSize = q.length;

      const level = [];
      for (let i = 0; i < levelSize; i++) {
        const node = q.shift();

        level.push(node.val);
        if (root instanceof TreeNode) {
          if (node.left !== null) q.push(node.left);
          if (node.right !== null) q.push(node.right);
        }
        res.push(level.slice());
      }
    }

    return res;
  }
}

if (require.main === module) {
  let t = new BiTree([3, 9, 20, null, null, 15, 17]);
  let res = Tree.levelOrder(t.root);
  console.log(res);
}
