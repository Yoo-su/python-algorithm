from collections import deque

def sol(head:ListNode):
    q:List=[]

    if not head:
        return True

    node=head

    while node is not None:
        q.append(node.val)
        node=node.next

    while len(q)>1:
        #리스트는 pop에 적합하지 않다. O(n)이 걸림
        if q.pop(0)!=q.pop():
            return False

    return True

def sol2(head:ListNode):
    q:deque()

    if not head:
        return True

    node=head

    while len(q)>1:
        if q.popleft()!=q.pop():
            return False

    return True

#pop할일 있으면 deque 써야 함!