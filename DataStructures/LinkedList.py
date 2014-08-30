class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value;
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        if self.head == None:
            self.head = self.Node(value)
            self.size = 1
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = self.Node(value)
            self.size += 1

    def remove(self, value):
        remove = False
        if self.head is not None:
            if self.head.value == value:
                self.head = self.head.next;
                remove = True

            else:
                temp = self.head
                while temp.next is not None:
                    if temp.next.value == value:
                        temp.next = temp.next.next
                        remove = True
                        break
                    temp = temp.next
            if remove is True:
                self.size -= 1
    
    def printMe(self):
        temp = self.head
        while temp is not None:
            print temp.value
            temp = temp.next

    def indexOf(self, value):
        found = False
        temp = self.head
        index = 0;

        while temp is not None:
            if temp.value == value:
                found = True
                break
            else:
                index += 1
                temp = temp.next

        if found is False:
            index = -1

        return index;

    def getSize(self):
        return self.size

        
            

