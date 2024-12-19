export class UnionFind {
  // 数组下标对应元素，值对应父节点
  parent: number[];

  constructor(size: number) {
    this.parent = new Array(size);
    for (let i = 0; i < size; i++) {
      this.parent[i] = i;
    }
  }

  find(x: number): number {
    this.validate(x);
    if (this.parent[x] === x) return x;
    return this.find(this.parent[x]);
  }

  union(x: number, y: number): void {
    this.validate(x, y);
    if (x === y) return;
    const rootX = this.find(x);
    const rootY = this.find(y);
    this.parent[rootX] = rootY;
  }

  isConnected(x: number, y: number): boolean {
    this.validate(x, y);
    return this.find(x) === this.find(y);
  }

  validate(...args: number[]): void {
    for (const x of args) {
      if (x < 0 || x >= this.parent.length) {
        throw new Error(`The element ${x} is out of bound of ${this.parent.length}.`);
      }
    }
  }
}

if (require.main === module) {
  // Example usage
  const uf = new UnionFind(10);

  // Perform union operations
  uf.union(1, 2);
  uf.union(2, 8);
  uf.union(7, 8);

  uf.union(3, 4);
  uf.union(5, 6);

  // Find the root of an element
  const root1 = uf.find(1);
  const root2 = uf.find(5);

  console.log('Root of 1: ' + root1);
  console.log('Root of 5: ' + root2);
  console.log('connected: ' + uf.isConnected(1, 5)); // false
}
