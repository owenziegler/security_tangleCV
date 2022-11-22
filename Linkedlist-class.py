class Node:  #creating a node class
    def __init__(self, data):
        self.item = data
        self.ref = None     #same as next null in c++
        self.weight = len(data)
        self.totalWeight = self.weight
        
class LinkedList:   #creating Linked list class
    def __init__(self):
        self.head = None
        self.tail = None
        self.numOfNodes = 0
    def increment(self,data):
        temp_previous = self.head
        while temp_previous is not None:
            temp_previous.weight += len(data)
            temp_previous = temp_previous.ref
            
            
    def insert_atstart(self,data):
        if self.head is None:   #if empty
            new_node = Node(data)
            #totalWeight = self.head    #going to store the node weight
            
            #new_node.ref = self.head
            self.head = new_node    #reference to the first node
            self.tail = new_node
        else:
            new_node = Node(data)
            #totalWeight = weight + self.ref     #adding current and next
            increment(data)
            tail.ref = new_node    #reference to the first node
            
            self.tail = new_node    #point to the newnode, the start
            self.numOfNodes += 1 
    
            
            
    
    def traverse(self): #print the linked list
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.item, " ")
                temp = temp.ref

    def validateNode(self):
        
        # if self.head is None:
        #     if self.numOfNodes is 0:
        #         return
        temp = self.head
        #if self.head

new_ll = LinkedList()   #creating an object for that class

new_ll.insert_atstart("Hello")    #just for testing
new_ll.insert_atstart("Bye")
new_ll.insert_atstart("Hi")

new_ll.traverse()
