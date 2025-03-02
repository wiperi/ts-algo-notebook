/*
 * @lc app=leetcode.cn id=146 lang=typescript
 *
 * [146] LRU 缓存
 */

// @lc code=start
class LRUCache {

  // Define the last entry in the map is the newest entry, while the
  // first entry is the oldest.

  // Every time a key is visited, update it as the newest by move it
  // to the tail of map.

  // If Cache capacity is full. Remove the first entry (oldest one).

  map = new Map();
  capacity: number;

  constructor(capacity: number) {
    this.capacity = capacity;
  }

  get(key: number): number {
    if (this.map.has(key) === false) {
      return -1;
    }
    this.moveToTail(key);
    return this.map.get(key);
  }

  put(key: number, value: number): void {
    if (this.map.has(key)) {
      // upate existing entry
      this.map.set(key, value);
      this.moveToTail(key);
    } else {
      // add new entry

      if (this.map.size === this.capacity) {
        // cache is full

        // remove first entry (oldest entry)
        this.map.delete(this.map.keys().next().value);
      }

      // add new entry
      this.map.set(key, value);
    }
  }

  // move entry to the tail of map
  moveToTail(key: number): void {
    const val = this.map.get(key);
    this.map.delete(key);
    this.map.set(key, val);
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
// @lc code=end
