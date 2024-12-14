import util from 'node:util';

export class __Node {
  val: number;
  children: __Node[];

  constructor(val?: number, children?: __Node[]) {
    this.val = val ?? 0;
    this.children = children ?? null;
  }
}

export class MultiTree {
  root: __Node;
  nodes: Map<number, __Node> = new Map();

  constructor(adjMap?: Map<number, number[]>) {
    if (!adjMap || !adjMap.size) {
      this.root = null;
      return;
    }

    this.root = new __Node(adjMap.keys().next().value);

    const q = [this.root];
    while (q.length) {
      const node = q.shift();

      this.nodes.set(node.val, node);

      const children = adjMap.get(node.val);
      if (children && children.length > 0) {
        checkLoop.call(this, node, children);

        node.children = children.map(v => new __Node(v));
        q.push(...node.children);
      } else {
        node.children = null;
      }
    }

    function checkLoop(node: __Node, children: number[]) {
      const badVal = children.find(v => this.nodes.has(v));
      if (badVal) {
        throw new Error(
          `Loop detected in adjacency map: ${node.val} -> ${badVal}, make sure all values are unique`
        );
      }
    }
  }

  [util.inspect.custom]() {
    return MultiTree.printTree(this.root);
  }

  static printTree(root: __Node): string {
    const lines: string[] = [];

    function dfs(node: __Node, prefix: string, isLast: boolean): void {
      if (!node) return;
      // Add the current node's value to the lines
      lines.push(`${prefix}${isLast ? '└─ ' : '├─ '}${node.val}`);

      // Prepare the prefix for child nodes
      const childPrefix = prefix + (isLast ? '   ' : '│  ');

      // Iterate over the children
      if (node.children && node.children.length > 0) {
        const lastIndex = node.children.length - 1;
        node.children.forEach((child, index) => {
          dfs(child, childPrefix, index === lastIndex);
        });
      }
    }

    // Start the DFS traversal from the root node
    dfs(root, '', true);

    // Join all lines into a single string
    return lines.join('\n');
  }
}

if (require.main === module) {
  const adjMap = new Map<number, number[]>();
  adjMap.set(0, [1, 2, 3, 10, 11]);
  adjMap.set(1, [4, 5]);
  adjMap.set(2, [6, 7]);
  adjMap.set(3, [8, 9, 12, 13]);
  const tree = new MultiTree(adjMap);
  // console.dir(tree, { depth: null });
  console.dir(tree.nodes, { depth: null });
  let res = MultiTree.printTree(tree.root);
  console.log(res);
}
