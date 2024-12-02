class ListNode<T = number> {
  val: T | null;
  next: ListNode<T> | null;

  constructor(val?: T, next?: ListNode<T> | null) {
    this.val = val ?? null;
    this.next = next ?? null;
  }
}

class List<T> {
  nodes: ListNode<T>[] = [];
  head: ListNode<T> | null = null;

  constructor();
  constructor(arr: T[]);
  constructor(arr?: T[]) {
    arr?.filter((v, i) => {
      this.nodes.push(new ListNode(v, null));
      i === 0 && (this.head = this.nodes[i]);
      return true;
    }).filter((v, i) => {
      this.nodes[i].next = this.nodes[i + 1] ?? null;
      return true;
    });
  }

  toString(): string {
    const printed: Set<ListNode<T>> = new Set();
    const res: string[] = [];

    const parse = (head: ListNode<T> | null): string => {
      let res = '';
      while (head) {
        printed.add(head);
        res += `${head.val}`;
        head.next && (res += ' -> ');
        head = head.next;
      }
      return res || 'null';
    };

    res.push('head: ' + parse(this.head));
    this.nodes.forEach(v => {
      if (printed.has(v)) return;
      res.push('fragment: ' + parse(v));
    });
    return res.join('\n');
  }

  tail(): ListNode<T> | null {
    let head = this.head;
    while (head?.next) {
      head = head.next;
    }
    return head;
  }

  push(val: T): void {
    const newNode = new ListNode(val, null);
    this.nodes.push(newNode);

    this.tail()!.next = newNode;
  }
}

function reverseList(head: ListNode<number> | null): ListNode<number> | null {
  if (head === null) {
    return null;
  }

  if (head.next === null) {
    return head;
  }

  const last = reverseList(head.next);

  head.next.next = head;
  head.next = null;

  return last;
}

function reverseListIter(head: ListNode | null) {
  if (head === null) return null;

  let prev = null;
  let curr = head;
  let next = curr.next;

  while (curr) {
    next = curr.next;

    curr.next = prev;

    prev = curr;

    if (!next) break;
    curr = next;
  }

  return curr;
}
const l = new List([1, 2, 3, 4, 5]);

l.head = reverseListIter(l.head);

console.log(l.toString());
