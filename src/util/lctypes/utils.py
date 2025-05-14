class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def listFrom(arr):
    """
    Convert an array to a linked list

    Args:
        arr: List of values to convert

    Returns:
        Head of the linked list
    """
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def listShow(head):
    """
    Convert a linked list to a string representation

    Args:
        head: Head of the linked list

    Returns:
        String representation of the linked list
    """
    if not head:
        return "[]"

    result = []
    current = head

    while current:
        result.append(str(current.val))
        current = current.next

    return "[" + " -> ".join(result) + "]"
