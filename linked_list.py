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
        """
        Returns the count/ len of the linked list
        Runs with O(n) time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        ads new node containing data at list head
        runs in constant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        """
        returns data for the node that matches the key.
        returns None if not found
        
        takes O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new node conatining data at index pos
        
        Insertion takes O(1), however finding at insertion takes O(n)

        Therefore, overall is O(n)
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            prev = current
            next = current.next_node

            prev.next_node = new
            new.next_node = next
    
    def remove_at_key(self, key):
        """
        Rempves node containing data mathcing key
        Returns node or None if does not exist

        Takes O(n) time
        """
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

    def __repr__(self):
        """
        prints all things in the list, with annotations.
        
        O(n) complexiy
        """
        nodes = []
        current = self.head
        while current:
            if current == self.head:
                nodes.append("[Head: %s]" %current.data)
            elif current.next_node == None:
                nodes.append("[Tail: %s]" %current.data)
            else:
                nodes.append("[%s]" %current.data)
            current = current.next_node
        return "->".join(nodes)
