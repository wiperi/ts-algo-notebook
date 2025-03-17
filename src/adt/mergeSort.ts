function mergeSort(nums: number[]): number[] {
  merge(0, nums.length);
  return nums;

  // 左闭右开区间 [lo, hi)
  function merge(lo: number, hi: number) {
    const midIndex = mid(lo, hi);
    if (hi - lo < 2) {
      return;
    }

    merge(lo, midIndex);
    merge(midIndex, hi);

    sort(lo, hi);
  }

  function sort(lo: number, hi: number) {
    const copy = nums.slice(lo, hi);
    const midIndex = mid(0, copy.length);

    let left = 0;
    let right = midIndex;
    let i = lo;

    while (left < midIndex && right < copy.length) {
      if (copy[left] <= copy[right]) {
        nums[i++] = copy[left++];
      } else {
        nums[i++] = copy[right++];
      }
    }

    // 处理剩余的元素
    while (left < midIndex) {
      nums[i++] = copy[left++];
    }
    while (right < copy.length) {
      nums[i++] = copy[right++];
    }
  }

  function mid(lo: number, hi: number) {
    return Math.floor((lo + hi) / 2);
  }
}

if (require.main === module) {
  console.log(mergeSort([-2, 3, -5]));
}

export {}