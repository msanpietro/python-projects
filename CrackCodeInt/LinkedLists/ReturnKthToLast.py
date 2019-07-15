#! /usr/bin/python

# 1) Creates unsorted linked list
# 2) Prints the list
# 3) print the kth to last element of the linked list


# Define a Node class that holds the following:
#    => data: store the value of the current list element
#    => next_node: stores the next Node in the Linked List. 
class Node(object):
    def __init__(self,data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self,new_next):
        self.next_node = new_next

    def printNode(self):
        print self.data,
        print " ===> ", 

# Define a LinkedList class the holds the following:
#    => head  : pointer to the head of the Linked List. Head is the 1st node

class SinglyLinkedList:
    # Note when list is first initialized it has no nodes so head is set to None
  def __init__(self,head=None):
        self.head = head
    
  def insert(self,data):
       new_node = Node(data)
       new_node.set_next(self.head)
       self.head = new_node

  def size(self):
      current = self.head
      count = 0 
      while current:
          count += 1
          current = current.get_next()
      return count

  def printList(self):
      current = self.head
      #print ( "the value of the head is %s" %(current.data) ) 
      count = 0 
      while current:
          count += 1
          if current.data is not None:
              current.printNode()
              current = current.get_next()
          else:
              return

  def search(self,data):
      current = self.head
      found = False
      while current and found is False:
          if current.get_data() == data:
              found = True
          else:
              current = current.get_next()
          if current is None:
              raise ValueError("Data not in list")
      return current
  
  # this function will delete ALL occurances of a value from the LL
  def delete(self,data):
      current = self.head
      previous = None
      found = False
      while current and found is False:
          if current.get_data() == data:
              found = True
          else:
              previous = current
              current = current.get_next()
      if current is None:
          raise ValueError("Data not in list")
      if previous is None:
          self.head = current.get_next()
      else:
          previous.set_next(current.get_next())
 
  def findkthtolastnode(self,k):
        p1 = self.head
        p2 = self.head

        # move p1 k nodes into the Linked List
        for i in range (1, k):
            if p1 == None:
                print "the k value is out of bounds"
                break
            else:
               p1 = p1.next_node
        # move p1 and p2 at the same rate until p1 hits end of Linked List
        while p1.next_node is not None:
            p1 = p1.next_node
            p2 = p2.next_node
        return p2
    

## Main
LL = SinglyLinkedList()
LL.insert(1)  # 1st node moves down to become tail when any nodes are added
LL.insert(2)  # 1st node moves down to become tail when any nodes are added
LL.insert(9)  # 1st node moves down to become tail when any nodes are added
LL.insert(6)  # 1st node moves down to become tail when any nodes are added
LL.insert(1)  # 1st node moves down to become tail when any nodes are added
LL.insert(3)  # 1st node moves down to become tail when any nodes are added
LL.insert(7)  # 1st node moves down to become tail when any nodes are added
LL.insert(8)  # 1st node moves down to become tail when any nodes are added
LL.insert(4)  # 1st node moves down to become tail when any nodes are added
LL.insert(7)  # 1st node moves down to become tail when any nodes are added
LL.insert(10)  ## this will be the head of the linked list

print "The Linked List is shown below........"
LL.printList() 
# find the kth to last element of the linked list
k = 4 
print "\n"
print ( "the value of k is %s" %(k) )
print ( "The %s th to last element of the linked list is..." %(k) )
LL.findkthtolastnode(k).printNode() 
