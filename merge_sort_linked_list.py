class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" %self.data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        current = self.head
        while current:
            if current == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current - current.next_node
                position -= 1
            prev = current
            next = current.next_node

            prev.next_node = new
            new.next_node = next
    
    def remove_at_key(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current
    
    def node_at_index(self, index):
        if index == 0:
            return self.head
        count = 0
        current = self.head
        while count < index:
            current = current.next_node
            count +=1
        return current
    
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current == self.head:
                nodes.append("[Head: %s]" %current.data)
                current = current.next_node
            elif current.next_node == None:
                nodes.append("[Tail %s]"%current.data)
            else:
                nodes.append(current.data)
                current = current.next_node
        return "->".join(nodes)

# -- algo --
def merge_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head() is None:
        return linked_list
    
    lefth, righth = split(linked_list)

    left = merge_sort(lefth)
    right = merge_sort(righth)

    merged_linked_list = merge(left, right)

    return merged_linked_list

def split(l):
    if l is None or l.head() is None:
        left = l
        right = None
        return left, right

    # getting the size
    s = l.size()
    # finding mp...
    mp = s // 2
    # subtract one, as size returns +1 (as its not indexes, it is len)
    mp_node = l.node_at_index(mp -1)
    
    # gving the left hand list the val of the whole linked list
    left = l
    # creating a new linked list obj
    right = LinkedList()
    # setting the beggining of that linked list as the head (mp) of the older list
    right.head = mp_node.next_node
    # deleting the connection/ reference of the next node from the right, as it is the head... splittin git into 2 seperate lists without connection
    mp_node.next_node = None

    return left, right

def merge(l, r):
    """
    Merges two linked lists, sorting by datain nodes

    Returns new (sorted) linked list
    """
    # output list
    new_l = LinkedList()
    # assign a temporary fake head that is disgaurded later
    new_l.add(0)

    current = new_l.head

    # obtain other heads...
    l_head = l.head
    r_head = r.head

    # itteration over l/ r until tail
    while l_head or r_head:
        if l_head.data < r_head.data:
            current.next_node = l_head
            l_head = l_head.next_node
        else:
            current.next_node = r_head
            r_head = r_head.next_node
    current.next_node

    head = new_l.head.next_node
    new_l.head = head

    return new_l