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

    def increment(self,data):
        temp_previous = self.head
        while temp_previous is not None:
            temp_previous.lastWeight = temp_previous.totalWeight
            temp_previous.totalWeight += len(data)
            temp_previous.lastNode = self.numOfNodes
            temp_previous = temp_previous.ref[0]
            
            
    def insert_at_current_node(self,data):
        if self.head is None:   #if empty
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            self.increment(data)
            self.tail.ref[0] = new_node     #reference to the first node            
            self.tail = new_node    #point to the newnode, the start
        self.numOfNodes += 1 
        new_node.currentNode = self.numOfNodes

    def insert_at_child_node(self, data):
        if self.head is None:   #if empty
            new_node = Node(data)
            self.head = new_node    #reference to the first node
            self.tail = new_node
        else:
            new_node = Node(data)
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
                for nextItem, currNode in enumerate(temp.ref):
                    print("",end="")
                print("Current Weight: ", temp.weight, " ", "Total Weight:",  temp.totalWeight, " ", "Last Total Weight: ", temp.lastWeight, " ", "Current Node: ", temp.currentNode, "Current Message: ", temp.item)
                temp = temp.ref[nextItem]

    def traverse_weight(self):
        if self.head is None:
            print("Nothing to print")
            return
        else:
            temp = self.head
            while temp is not None:
                for nextItem, currNode in enumerate(temp.ref):
                    print("",end="")
                temp = temp.ref[nextItem]            

def main():
    list = LinkedList()
    running = True
    while running:
        response1 = input("Would you like to add a new node, display the list, or quit? (add/add-child/display/quit): ")
        response1 = response1.upper()
        if response1 == "ADD" or response1 == "A":
            newdata = input("Input data of new node: ")
            list.insert_at_current_node(newdata)
        elif response1 == "DISPLAY" or response1 == "D":
            print("Displaying information:")
            list.traverse()
        elif response1 == "ADD-CHILD" or response1 == "AC":
            newdata = input("Input data of new node: ")
            list.insert_at_child_node(newdata)
        elif response1 == "QUIT" or response1 == "Q":
            print("Exiting...")
            exit()
        else:
            print("Invalid response. Please try again")
            
if __name__ == "__main__":
    main()
