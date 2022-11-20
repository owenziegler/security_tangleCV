class Node:  #creating a node class
    def __init__(self, data):
        self.item = data
        self.ref = None     #same as next null in c++
    
class LinkedList:   #creating Linked list class
    def __init__(self):
        self.head = None
    
    def insert_atstart(self,data):
        new_node = Node(data)
        new_node.ref = self.head    #reference to the first node
        self.head = new_node    #point to the newnode, the start 
    
    def traverse(self): #print the linked list
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.item, " ")
                temp = temp.ref
        
new_ll = LinkedList()   #creating an object for that class

new_ll.insert_atstart(5)    #just for testing
new_ll.insert_atstart(4)
new_ll.insert_atstart(3)

new_ll.traverse()

        
        