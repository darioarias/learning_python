



class Node(object):
    def __init__(self, value, next = None, prev = None) -> None:
        self.value = value
        self.next = next 
        self.prev = prev
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.value!r})'



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.next = n2 
n2.prev = n1 

n2.next = n3 
n3.prev = n2 

n3.next = n4 
n4.prev = n3 

n4.next = n5 
n5.prev = n4 

n5.next = n6 
n6.prev = n5

from functools import partial

def nodes_gexp(head: Node = None) -> Node:
    while head:
        # return head 
        yield head
        # print(head)
        head = head.next 

# def nodes(items, indx):
#     return items[indx]
# # print(nodes_gexp(n1))     

root = partial(nodes_gexp, n1)

# print(root())
# for n in root:
#     print(n)

nodes_itr = iter(root, None)


for node in nodes_itr:
    print(node)
