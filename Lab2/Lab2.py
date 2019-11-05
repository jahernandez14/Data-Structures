'''
Julio Hernandez
88382550
Lab #2
CS 2302 TTR

Goal:
The purpose of this lab is to traverse a txt file full of passwords and be able to read the information
enter it into a linked like and order it with the use of merge sort and bubble sort.
'''

#Node class
class Node(object):

    #Constructor
    def __init__ (self,password,count,next = None):
        self.password = password
        self.count = count
        self.next = next

    #setters
    def setPassword(self, password):
        self.password = password
    def setCount(self, count):
        self.count = count
    def setNext(self, next):
        self.next = next

    #getters
    def getPassword(self):
        return self.password
    def getCount(self):
        return self.count
    def getNext(self):
        return self.next

#Linked List Class
class LinkedList(object):

    #method to create head of linked list
    def __init__(self, head = None):
        self.head = head

    #method to insert items into the linked list
    def insert(self, password, count):
        newNode = Node(password, count)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    #method to compare nodes in the link list and create a link list with no repeated nodes
    def compare(self, password, count):
        current = self.head
        repeat = False
        while current and repeat is False:
            if current.getPassword() == password:
                current.setCount(current.getCount() + 1)
                repeat = True
            else:
                current = current.next

        if current is None:
            return 1

    #method to determine the size of the linked list, it was not needed but i added it just in case
    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.getNext()
        return size

    #method to print link list
    def printList(self):
        temp = self.head
        while temp:
           print("Password: %s Count: %d" % (temp.password, temp.count))
           temp = temp.next
        print("**********************************\n")

    #method to print link list of top 20 count nodes
    def printTop20(self):
        counter = 0
        temp = self.head
        while counter < 20 and temp != None:
            print("Password: %s Count: %d" % (temp.password, temp.count))
            temp = temp.next
            counter += 1
        print("**********************************\n")

"""Solution A"""
#method that goes through a txt file and only adds lines that do no repeat
def trim():
    passwordList = LinkedList()
    empty = True
    with open("test.txt", "r") as file:
        for line in file:
            try:
                if empty == True:
                    passwordList.insert(line.split()[1], 0)
                    empty = False
                result = passwordList.compare(line.split()[1], 1)
                if result == 1:
                    passwordList.insert(line.split()[1], 1)
                #exception to protect against skipped lines
            except IndexError:
                pass
            continue
    return passwordList

#method to sort the list by count values
def bubbleSort(self):
     if self.head == None:
         return
     #loop to compare count of next node and keep checking until None is reached
     for i in range(self.size()):
         #loop repeats the size of the list
        temp = self.head
        while temp.next is not None:
            if temp.getCount() < temp.next.getCount():
                tempCount, tempPassword = temp.getCount(), temp.getPassword()
                temp.setCount(temp.next.getCount())
                temp.setPassword(temp.next.getPassword())
                temp.next.setCount(tempCount)
                temp.next.setPassword(tempPassword)
            temp = temp.next

"""Solution B"""
#method to read a file and use a dictionary to count the number of repetitions
def DictionaryRead():
    #key list
    password_dict = {}
    passwordList = LinkedList()
    #loop to go through the txt file
    with open("test.txt", "r") as file:
        for line in file:
            try:
                current_line = line.split()[1]
                if current_line in password_dict:
                    password_dict[current_line] = password_dict[current_line] + 1
                else:
                    password_dict[current_line] = 1
            except IndexError:
                pass
        #loop to populate linked list
    for item, i in password_dict.items():
        passwordList.insert(item, i)
    return passwordList

#methof to sort linked list using merge Sort
def mergeLists(left, right):
    if left is None:
        return right
    if right is None:
        return left
    #recursive calls to merge lists in the correct order
    if left.getCount() >= right.getCount():
        temp = left
        temp.next = mergeLists(left.next, right)
    else:
        temp = right
        temp.next = mergeLists(left, right.next)
    return temp

#Defining function which will sort the linked list using mergeSort
def mergeSort(head):
    #base case
    if head is None or head.next is None:
        return head
    #method call to split left and right
    left, right = divideLists(head)
    #sort node
    left = mergeSort(left)
    right = mergeSort(right)
    #merge left and right node
    head = mergeLists(left,right)
    return head

#find mid and split list using slow fast
def divideLists(head):
    #varibles to track position
    slow = head
    fast = head

    if fast:
        fast = fast.next
    #loop to find mid by moving position of fast slow
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid

#main method
def main():
    print("*************Password Results*************\n")
    print("**********Solution A**************")

    #Solution A
    #password list is created and is "trimmed" to not include duplicates
    passwordList = trim()
    #sort method is called
    bubbleSort(passwordList)
    #print top 20 occurrences
    passwordList.printTop20()

    #Solution B
    print("**********Solution B**************")
    #create linked list using dictionary
    dictList = DictionaryRead()
    #sort dictionary list using merge sort
    mergeSort(dictList.head)
    #print top 20 occurrences in dictionary list
    dictList.printTop20()

main()
#end of program
