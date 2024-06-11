

class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def top(self):
        if (not self.isEmpty()):
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items


class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    # Add an item to the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # Delete an item from the queue
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items
    

class LinkedList:
    pass


class BinaryTreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNode:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class GraphNode:

    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []