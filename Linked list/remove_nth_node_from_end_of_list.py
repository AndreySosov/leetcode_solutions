def middleNode(head, target):
    start = head
    while start != target:
        start = start.next
    start = target.next
    return start