import util from 'node:util';

export class __Node {
  val: any;
  children: __Node[];

  constructor(val?: any, children?: __Node[]) {
    this.val = val;
    this.children = children ?? [];
  }
}

export class MultiTree {
  root: __Node;
  nodes: Map<number, __Node> = new Map();

  constructor(edges?: Map<any, any[]>) {
    if (!edges || !edges.size) {
      this.root = new __Node();
      return;
    }

    this.root = new __Node(edges.keys().next().value);

    const que = [this.root];
    while (que.length) {
      const node = que.shift();

      this.nodes.set(node.val, node);

      const childValInputs = edges.get(node.val);
      if (childValInputs && childValInputs.length > 0) {
        checkLoop.call(this, node, childValInputs);

        node.children = childValInputs.map(v => new __Node(v));
        que.push(...node.children);
      }
    }

    function checkLoop(node: __Node, children: any[]) {
      const duplicatedVal = children.find(v => this.nodes.has(v));
      if (duplicatedVal) {
        throw new Error(
          `Loop detected in adjacency map: ${node.val} -> ${duplicatedVal}, make sure all values are unique`
        );
      }
    }
  }

  [util.inspect.custom]() {
    return MultiTree.printTree(this.root);
  }

  static printTree(root: __Node): string {
    const lines: string[] = [];

    // Start the DFS traversal from the root node
    dfs(root, '', true);

    // Join all lines into a single string
    return lines.join('\n');

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
  }
}

if (require.main === module) {
  const tree = new MultiTree(new Map([
    [1, [2,3,4, 5]],
    [5,[6,7,undefined]],
    [undefined, [8,9]],
    [9, [null]],
    [null, ['hello', ['world']]]
  ]))
  // console.dir(tree, { depth: null });
  console.dir(tree.nodes, { depth: null });
  let res = MultiTree.printTree(tree.root);
  console.log(res);
}
