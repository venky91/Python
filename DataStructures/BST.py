class BST:
    class Pair:
        def __init__(self, parent, root):
            self.parent = parent
            self.root = root

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
                        
    def remove(self,value):
        self.findNodeToDelete(self.root, value, None)

    def findNodeToDelete(self, root, value, parent):

        parent = None
        while root is not None:
            if root.value == value:
                self.removeNode(root, parent)
                break
            elif root.value < value:
                parent = root
                root = root.right
            
            else:
                parent = root
                root = root.left

    def removeNode(self, root, parent):

        processPredecessor = False;

        if parent is None:     # super root
            if self.root.left is None:
                self.root = self.root.right
            elif self.root.right is None:
                self.root = self.root.left
            else:
                processPredecessor = True

        else:
            if root.left is None:
                if parent.left is root:
                    parent.left = root.right
                else:
                    parent.right = root.right
            elif root.right is None:
                if parent.left is root:
                    parent.left = root.left
                else:
                    parent.right = root.left
            else:
                processPredecessor = True

        if processPredecessor is True:
                predecessorPair = self.getPredecessor(root.left, root)
                rightMostNode = predecessorPair.root
                rightMostParent = predecessorPair.parent
                root.value = rightMostNode.value
                self.removeNode(rightMostNode, rightMostParent)

    def getPredecessor(self, root, parent):

        while root.right is not None:
            parent = root
            root = root.right

        return self.Pair(parent, root)
        
                    


