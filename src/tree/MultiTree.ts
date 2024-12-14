export class __Node {
  val: number;
  children: __Node[];

  constructor(val?: number, children?: __Node[]) {
    this.val = val === undefined ? 0 : val;
    this.children = children === undefined ? [] : children;
  }
}
