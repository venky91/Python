class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = self.Node(value)
        
        else:
            temp = self.root
            
            while True:
                if temp.value > value:
                    if temp.left is None:
                        temp.left = self.Node(value)
                        break
                    else:
                        temp = temp.next
                else:
                    if temp.right is None:
                        temp.right = self.Node(value)
                        break
                    else:
                        temp = temp.right

                    


