class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self):
        head_node = Node(value=None)
        self.head=head_node

    def insert(self, value, pos=0):
        """
        insert at a specified position
        :param value:
        :return:
        """
        p=self.head
        if pos !=0:
            for i in range(pos):
                if p is not None:
                    p = p.next
                else:
                    raise ValueError('position overflow')

        new_node=Node(value)
        new_node.next=p.next
        p.next=new_node

    def search(self,value):
        p=self.head.next
        pos=1
        while p:
            if p.value == value:
                return pos
            p=p.next
            pos = pos + 1
        raise RuntimeError('Not found value in linked list')

    def delete(self, pos):
        p = self.head
        if pos != 0:
            for i in range(pos-1):
                if p is not None:
                    p = p.next
                else:
                    raise ValueError('position overflow')

        target_delete_node = p.next
        p.next = p.next.next
        del target_delete_node

    def __str__(self):
        p=self.head.next
        value_list=[]
        while p:
            value_list.append(p.value)
            p=p.next
        return ','.join(str(v) for v in value_list)

    def reverse(self):




my_ll = LinkedList()
for i in range(5):
    my_ll.insert(i,pos=i)
print(my_ll)

my_ll.delete(5)
print(my_ll)
my_ll.delete(3)
print(my_ll)

print(my_ll.search(1))
print(my_ll.search(0))
#print(my_ll.search(2))