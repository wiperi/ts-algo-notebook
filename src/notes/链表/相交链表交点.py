from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


def getIntersectionNode(self, ha: Optional[ListNode], hb: Optional[ListNode]) -> Optional[ListNode]:
    """
    Elegant solution using the two-pointer technique.
    If two linked lists intersect, pointers will meet after switching paths.
    If they don't intersect, both pointers will reach None simultaneously.
    """
    if not ha or not hb:
        return None

    a, b = ha, hb

    # When a pointer reaches the end, redirect it to the head of the other list
    # This ensures both pointers travel the same distance before meeting
    while a != b:
        a = hb if a is None else a.next
        b = ha if b is None else b.next

    return a  # Either the intersection point or None if no intersection
