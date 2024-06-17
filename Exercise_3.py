# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class LinkedList: 
  
    def __init__(self): 
        self.stack = Node(None)
  
    def push(self, new_data): 
        if self.stack.data == None:
            self.stack.data = new_data
        else:
            new_node = Node(new_data)
            new_node.next = self.stack
            self.stack = new_node
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        slow = self.stack
        fast = self.stack

        if self.stack != None:
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
            print("The middle element is: ", slow.data) 

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
