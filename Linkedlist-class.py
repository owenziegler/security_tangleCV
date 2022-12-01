import messageMaker

class Node:  #creating a node class
    def __init__(self, data):
        self.item = data           #This is where the message is stored.
        self.Next = None           #This is the default "next" node. It's set to null.
        self.ref = [self.Next]     #same as next null in c++. We wrote our references this way
                                   #To signify that one node can have multiple references.
        self.weight = len(data)    #This is the weight of the node.
        self.totalWeight = self.weight  #This is the total weight of the node.
        self.lastWeight = 0        #This signifies the previous "totalweight" value
        self.currentNode = 0       #This stores the number of child nodes under the current node.
        self.lastNode = 0          #This stores the previous number of child nodes.
        self.cipherText = ""       #This stores the ciphertext

class LinkedList:   #creating Linked list class
    def __init__(self):
        self.head = None
        self.tail = None
        self.numOfNodes = 0

    #The increment function updates all of the values.
    def increment(self,data):
        temp_previous = self.head
        while temp_previous is not None:
            temp_previous.lastWeight = temp_previous.totalWeight
            temp_previous.totalWeight += len(data)
            temp_previous.lastNode = self.numOfNodes
            temp_previous = temp_previous.ref[0]
            
    #The "insert_at_current_node" function inserts a child node and sets the current 
    #node to that child node.
    def insert_at_current_node(self,data):
        if self.head is None:   #if empty
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            AES = messageMaker.AESCipher("key phrase")
            new_node.cipherText = AES.encrypt(data)
        else:
            new_node = Node(data)
            self.increment(data)
            self.tail.ref[0] = new_node     #reference to the first node            
            self.tail = new_node    #point to the newnode, the start
            AES = messageMaker.AESCipher("key phrase")
            new_node.cipherText = AES.encrypt(data)

        self.numOfNodes += 1 
        new_node.currentNode = self.numOfNodes

    #The "insert_at_child_node" function inserts a child node but does NOT set the
    #current node to that child node.
    def insert_at_child_node(self, data):
        if self.head is None:   #if empty
            new_node = Node(data)
            self.head = new_node    #reference to the first node
            self.tail = new_node
            AES = messageMaker.AESCipher("key phrase")
            new_node.cipherText = AES.encrypt(data)
        else:
            new_node = Node(data)
            self.increment(data)
            self.tail.ref.append(new_node)     #reference to the first node
            AES = messageMaker.AESCipher("key phrase")
            new_node.cipherText = AES.encrypt(data)
            self.tail = new_node    #point to the newnode, the start
        self.numOfNodes += 1 
        new_node.currentNode = self.numOfNodes            
    
    #This prints out the data from all the nodes.
    def traverse(self): #print the linked list
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                for nextItem, currNode in enumerate(temp.ref):
                    print("",end="")
                print("Current Weight: ", temp.weight, " ", "Total Weight:",  temp.totalWeight, " ", "Last Total Weight: ", temp.lastWeight, " ", "Current Node: ", temp.currentNode, "Current Message: ", temp.item, "\nCiphertext: ", temp.cipherText, "\n")
                temp = temp.ref[nextItem]

def main():
    list = LinkedList()
    running = True
    #This runs the program.
    while running:
        #This takes an input from the user.
        response1 = input("Would you like to add a new node, display the list, or quit? (add/add-child/display/quit): ")
        #This sets the input so it's all capitalized -- so capitalization isn't a worry for the user.
        response1 = response1.upper()
        #This checks the user resposes.
        if response1 == "ADD" or response1 == "A":
            newdata = input("Input data of new node: ")
            list.insert_at_current_node(newdata)
        elif response1 == "DISPLAY" or response1 == "D":
            print("Displaying information:\n")
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
