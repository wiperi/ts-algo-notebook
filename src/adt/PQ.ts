import * as util from 'util';

export class minPQ {
  private heap: number[] = [];

  /**
   * Creates a new min priority queue
   */
  constructor() {
    // No comparator needed
  }

  /**
   * Add an element to the priority queue
   * @param value The value to add
   */
  enqueue(value: number): void {
    // Add the element to the end of the heap
    this.heap.push(value);
    // Bubble up to maintain the heap property
    this.bubbleUp(this.size() - 1);
  }

  /**
   * Remove and return the highest priority element
   * @returns The highest priority element or undefined if queue is empty
   */
  dequeue(): number | undefined {
    if (this.isEmpty()) return undefined;

    const min = this.heap[0];
    const last = this.heap.pop()!;
    
    if (this.size() > 0) {
      this.heap[0] = last;
      this.bubbleDown(0);
    }

    return min;
  }

  /**
   * View the highest priority element without removing it
   * @returns The highest priority element or undefined if queue is empty
   */
  peek(): number | undefined {
    return this.isEmpty() ? undefined : this.heap[0];
  }

  /**
   * Check if the queue is empty
   * @returns true if empty, false otherwise
   */
  isEmpty(): boolean {
    return this.heap.length === 0;
  }

  /**
   * Get the number of elements in the queue
   * @returns The size of the queue
   */
  size(): number {
    return this.heap.length;
  }

  /**
   * Move an element up the heap until heap property is restored
   * @param index The index of the element to move
   */
  private bubbleUp(index: number): void {
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      
      // If parent has higher priority (smaller value for min heap), stop
      if (this.heap[parentIndex] <= this.heap[index]) {
        break;
      }
      
      // Swap with parent
      [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
      index = parentIndex;
    }
  }

  /**
   * Move an element down the heap until heap property is restored
   * @param index The index of the element to move
   */
  private bubbleDown(index: number): void {
    const lastIndex = this.size() - 1;
    
    while (true) {
      const leftChildIndex = 2 * index + 1;
      const rightChildIndex = 2 * index + 2;
      
      // Find the smallest among node and its two children
      let smallestIndex = index;

      if (leftChildIndex <= lastIndex && 
          this.heap[leftChildIndex] < this.heap[smallestIndex]) {
        smallestIndex = leftChildIndex;
      }
      
      if (rightChildIndex <= lastIndex && 
          this.heap[rightChildIndex] < this.heap[smallestIndex]) {
        smallestIndex = rightChildIndex;
      }
      
      // If smallest is current node, heap property is satisfied
      if (smallestIndex === index) {
        break;
      }
      
      // Swap with the smaller child
      [this.heap[index], this.heap[smallestIndex]] = [this.heap[smallestIndex], this.heap[index]];
      index = smallestIndex;
    }
  }

  /**
   * Get a copy of the internal heap array
   * @returns A copy of the heap array
   */
  toArray(): number[] {
    return [...this.heap];
  }

  /**
   * Custom toString method
   */
  toString(): string {
    return `PriorityQueue [${this.heap.join(', ')}]`;
  }

  /**
   * Custom Node.js inspect method
   */
  [util.inspect.custom](): string {
    return this.toString();
  }
}

// Example usage
if (require.main === module) {
  const pq = new minPQ();
  
  // Add some elements
  pq.enqueue(5);
  pq.enqueue(3);
  pq.enqueue(7);
  pq.enqueue(1);
  
  console.log(`Queue: ${pq}`);
  console.log(`Size: ${pq.size()}`);
  console.log(`Peek: ${pq.peek()}`);
  
  console.log("\nDequeuing elements:");
  while (!pq.isEmpty()) {
    console.log(`Dequeued: ${pq.dequeue()}`);
  }
}
