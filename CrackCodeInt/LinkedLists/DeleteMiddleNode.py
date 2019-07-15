#! /usr/bin/python

# 1) Creates unsorted linked list
# 2) Prints the list
# 3) Without being given access to the head of the Linked List delete a "middle node" of the Linked List. ie any node not head or end but not the exact middle
# 4) Note that this problem requires each Node of the linked list to have a unique value

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
  def deleteNode(self,data):
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

  def deleteANodeWithoutAccessToHead(self,data):
      midnode = Node(data)
      #if n is None or n.next_node is None:
      #    print "in here"
      #    return False  ## can't remove the next node if this is the end of the list
      midnode.data = midnode.next_node.data
      midnode.next_node = midnode.next_node.next_node 
      print "shit"

## Main
LL = SinglyLinkedList()
LL.insert(1)  # 1st node moves down to become tail when any nodes are added
LL.insert(2)  # 1st node moves down to become tail when any nodes are added
LL.insert(9)  # 1st node moves down to become tail when any nodes are added
LL.insert(6)  # 1st node moves down to become tail when any nodes are added
LL.insert(5)  # 1st node moves down to become tail when any nodes are added
LL.insert(3)  # 1st node moves down to become tail when any nodes are added
LL.insert(7)  # 1st node moves down to become tail when any nodes are added
LL.insert(8)  # 1st node moves down to become tail when any nodes are added
LL.insert(4)  # 1st node moves down to become tail when any nodes are added
LL.insert(11)  # 1st node moves down to become tail when any nodes are added
LL.insert(10)  ## this will be the head of the linked list

print "The Linked List is shown below........"
LL.printList() 
# Without being given access to the head of the Linked list Delete a Node in the middle of the Linked List
# Given Node N we will first verify next node is not None. ie. our node is the last node
# and then we will delete the next node since this is all we have access to
print "\n"
print "input the node you want to delete"
data_value = 8
print ( "the data value of the node is %s " %(data_value) )
#LL.deleteNode(8)

LL.deleteANodeWithoutAccessToHead(data_value)
LL.printList()




