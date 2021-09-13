class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
    
class MyCalendar(object):
    def __init__(self):
        self.root = None
    
    def book_helper(self, start, end, node):
        if start >= node.end:
            if node.right:
                return self.book_helper(start, end, node.right)
            else:
                node.right = Node(start, end)
                return True
        elif end <= node.start:
            if node.left:
                return self.book_helper(start, end, node.left)
            else:
                node.left = Node(start, end)
                return True
        else:
            return False
    
    
    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.book_helper(start, end, self.root)
