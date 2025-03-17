/**
 * A node in the linked list for handling collisions
 */
class HashNode<T> {
  key: number;
  value: T;
  next: HashNode<T> | null;

  constructor(key: number, value: T) {
    this.key = key;
    this.value = value;
    this.next = null;
  }
}

/**
 * A simple HashMap implementation mapping number keys to any value
 */
export class HashMap<T> {
  private buckets: Array<HashNode<T> | null>;
  private size: number;
  private capacity: number;

  /**
   * Creates a new HashMap with the given capacity
   * @param capacity The initial capacity of the HashMap
   */
  constructor(capacity: number = 16) {
    this.capacity = capacity;
    this.size = 0;
    this.buckets = new Array(capacity).fill(null);
  }

  /**
   * Hash function to convert a key into an array index
   * @param key The key to hash
   * @returns Array index
   */
  private hash(key: number): number {
    // Simple hash function for numbers
    return Math.abs(key) % this.capacity;
  }

  /**
   * Sets a key-value pair in the HashMap
   * @param key The key (number)
   * @param value The value to store
   */
  set(key: number, value: T): void {
    const index = this.hash(key);
    const newNode = new HashNode(key, value);

    // If the bucket is empty, place the node directly
    if (!this.buckets[index]) {
      this.buckets[index] = newNode;
      this.size++;
      return;
    }

    // Handle collision with chaining
    let current = this.buckets[index] as HashNode<T>;
    let previous: HashNode<T> | null = null;

    // Check if key already exists in chain
    while (current) {
      if (current.key === key) {
        // Update existing key
        current.value = value;
        return;
      }
      previous = current;
      current = current.next as HashNode<T>;
    }

    // Add new node to end of chain
    if (previous) {
      previous.next = newNode;
    }
    this.size++;
  }

  /**
   * Gets the value for a key
   * @param key The key to look up
   * @returns The value or undefined if key doesn't exist
   */
  get(key: number): T | undefined {
    const index = this.hash(key);
    let current = this.buckets[index];

    while (current) {
      if (current.key === key) {
        return current.value;
      }
      current = current.next;
    }

    return undefined;
  }

  /**
   * Deletes a key-value pair from the HashMap
   * @param key The key to delete
   * @returns True if deletion was successful, false if key wasn't found
   */
  delete(key: number): boolean {
    const index = this.hash(key);
    let current = this.buckets[index];
    let previous: HashNode<T> | null = null;

    while (current) {
      if (current.key === key) {
        // Key found, remove node
        if (previous) {
          previous.next = current.next;
        } else {
          // It's the first node in the chain
          this.buckets[index] = current.next;
        }
        this.size--;
        return true;
      }
      previous = current;
      current = current.next;
    }

    return false; // Key not found
  }

  /**
   * Checks if a key exists in the HashMap
   * @param key The key to check
   * @returns True if the key exists
   */
  has(key: number): boolean {
    return this.get(key) !== undefined;
  }

  /**
   * Returns the number of entries in the HashMap
   * @returns The HashMap size
   */
  getSize(): number {
    return this.size;
  }

  /**
   * Clears all entries from the HashMap
   */
  clear(): void {
    this.buckets = new Array(this.capacity).fill(null);
    this.size = 0;
  }
}

if (require.main === module) {
  // Create a new HashMap
  const map = new HashMap<string>(10);
  
  // Add some key-value pairs
  map.set(1, "one");
  map.set(11, "eleven"); // Will hash to the same bucket as 1
  map.set(42, "forty-two");
  
  // Get values
  console.log("Value for key 1:", map.get(1));
  console.log("Value for key 11:", map.get(11));
  console.log("Value for key 42:", map.get(42));
  console.log("Value for non-existent key 100:", map.get(100));
  
  // Check if keys exist
  console.log("Has key 42:", map.has(42));
  console.log("Has key 100:", map.has(100));
  
  // Check size
  console.log("Map size:", map.getSize());
  
  // Update a value
  map.set(42, "updated forty-two");
  console.log("Updated value for key 42:", map.get(42));
  
  // Delete a key
  console.log("Delete key 11:", map.delete(11));
  console.log("Map size after deletion:", map.getSize());
  console.log("Value for key 11 after deletion:", map.get(11));
  
  // Clear the map
  map.clear();
  console.log("Map size after clear:", map.getSize());
}