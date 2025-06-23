# LCT (LeetCode Types)

A simple package providing common data structures for algorithm problems.

## Installation

```bash
pip install -e .
```

## Usage

You can import ListNode and TreeNode directly from the lct package:

```python
from lct import ListNode, TreeNode

# Create a linked list
node = ListNode(1)
node.next = ListNode(2)

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
``` 