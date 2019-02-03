class Node(object):

    def __init__(self,value):
    
        self.value = value
        self.nextnode = None

A = Node(1)
B = Node(2)

A.nextnode = B
print(A.nextnode.value)
