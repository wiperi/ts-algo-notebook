import { BiTree, TreeNode } from './BiTree';
import { _Node, MultiTree } from './MultiTree';

function levelOrder(root: TreeNode): any[] {
  const res = [];

  const q = [root];

  while (q.length !== 0) {
    const levelSize = q.length;

    const level = [];

    for (let i = 0; i < levelSize; i++) {
      // i = 元素在每一层中出现的次序
      const node = q.shift();

      level.push(node.val);

      if (node.left !== null) q.push(node.left);
      if (node.right !== null) q.push(node.right);
    }

    res.push(level.slice());
  }

  return res;
}

function levelOrderMultiTree(root: _Node) {
  const res = [];

  const q = [root];

  while (q.length !== 0) {
    const levelSize = q.length;

    const level = [];

    for (let i = 0; i < levelSize; i++) {
      const node = q.shift();

      level.push(node.val);

      node.children.forEach(c => q.push(c));
    }

    res.push(level.slice());
  }

  return res;
}

if (require.main === module) {
  let t = new BiTree([3, 9, 20, null, null, 15, 17]);
  let res = levelOrder(t.root);
  console.log(res);
  console.assert(JSON.stringify(res) === JSON.stringify([[3], [9, 20], [15, 17]]));

  let mt = new MultiTree(new Map([[1, [2, 3, 4, 5, 6]]]));
  res = levelOrderMultiTree(mt.root);
  console.log(res);
  console.assert(JSON.stringify(res) === JSON.stringify([[1], [2, 3, 4, 5, 6]]));
}

export default function (root: TreeNode | _Node) {
  if (root instanceof TreeNode) return levelOrder(root);
  if (root instanceof _Node) return levelOrderMultiTree(root);
}
