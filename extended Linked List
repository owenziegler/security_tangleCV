class Node:  #creating a node class
    def __init__(self, data):
        self.item = data
        self.Next = None
        self.ref = [self.Next]     #same as next null in c++
        self.weight = len(data)
        self.totalWeight = self.weight
        self.lastWeight = 0
        self.currentNode = 0
        self.lastNode = 0
        
class LinkedList:   #creating Linked list class
    def __init__(self):
        self.head = None
        self.tail = None
        self.numOfNodes = 0
        #self.lastnum_nodes

    def increment(self,data):
        temp_previous = self.head
        while temp_previous is not None:
            temp_previous.lastWeight = temp_previous.totalWeight
            temp_previous.totalWeight += len(data)
            temp_previous.lastNode = self.numOfNodes
            #temp_previous.currentNode += 1
            temp_previous = temp_previous.ref[0]
            
            
    def insert_at_current_node(self,data):
        if self.head is None:   #if empty
            new_node = Node(data)
            #totalWeight = self.head    #going to store the node weight
            
            #new_node.ref = self.head
            self.head = new_node    #reference to the first node
            self.tail = new_node
        else:
            new_node = Node(data)
            #totalWeight = weight + self.ref     #adding current and next
            self.increment(data)
            self.tail.ref[0] = new_node     #reference to the first node
            
            self.tail = new_node    #point to the newnode, the start
        self.numOfNodes += 1 
        new_node.currentNode = self.numOfNodes

    def insert_at_child_node(self, data):
        if self.head is None:   #if empty
            new_node = Node(data)
            #totalWeight = self.head    #going to store the node weight
            
            #new_node.ref = self.head
            self.head = new_node    #reference to the first node
            self.tail = new_node
        else:
            new_node = Node(data)
            #totalWeight = weight + self.ref     #adding current and next
            self.increment(data)
            self.tail.ref.append(new_node)     #reference to the first node
            
            self.tail = new_node    #point to the newnode, the start
        self.numOfNodes += 1 
        new_node.currentNode = self.numOfNodes            
    
    def traverse(self): #print the linked list
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                temp = temp.ref[0]

    def traverse_weight(self):
        if self.head is None:
            print("Nothing to print")
            return
        else:
            temp = self.head
            while temp is not None:
                for nextItem, currNode in enumerate(temp.ref):
                    print("",end="")
                print("Current Weight: ", temp.weight, " ", "Total Weight:",  temp.totalWeight, " ", "Last Total Weight: ", temp.lastWeight, " ", "Current Node: ", temp.currentNode, " ", "Last Node: ", temp.lastNode)
                temp = temp.ref[nextItem]
                #temp = temp.ref[0]

    def check_diff(self):
        if self.head.totalWeight < self.head.lastWeight:
            print("A problem have occured...")
        #elif self.head.totalWeight > self.head.lastWeight and self.numOfNodes:
            

    def validateNode(self):
        
        # if self.head is None:
        #     if self.numOfNodes is 0:
        #         return
        temp = self.head
        #if self.head

new_ll = LinkedList()   #creating an object for that class

new_ll.insert_at_current_node("Hello")    #just for testing
new_ll.insert_at_child_node("Seatbelt unbuckled")
new_ll.insert_at_current_node("Bye")
new_ll.insert_at_current_node("Hi")
new_ll.insert_at_child_node("Stop Right There!")

new_ll.traverse()
new_ll.traverse_weight()
