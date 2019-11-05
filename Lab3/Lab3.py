'''
Julio Hernandez
88382550
Lab#3
The purpose of this lab is to read a txt file and insert the words into a tree.
After doing this we are instructed to check the anagrams to the user inputed word.
'''

#Please note that a lot of this code is derived from zybooks. The the lab description we were instructed to use it as a guid

#node class for avl tree
class Node:
    #node class constructor
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    #method to check if the tree is balanced. This must be checked after every insertion
    def getBalance(self):
        heightOfLeft = -1
        if self.left is not None:
            heightOfLeft = self.left.height

        heightOfRight = -1
        if self.right is not None:
            heightOfRight = self.right.height

        return heightOfLeft - heightOfRight

    #method to calculate the height after every insertion
    #in addition this method must be called whenever insertion is processed to check if the tree is still balanced
    def calculateHeight(self):
        heightOfLeft = -1
        if self.left is not None:
            heightOfLeft = self.left.height

        heightOfRight = -1
        if self.right is not None:
            heightOfRight = self.right.height

        self.height = max(heightOfLeft, heightOfRight) + 1

    #method to change the child based on balancing results
    def updateChild(self, currentChild, newChild):
        if self.left is currentChild:
            return self.assignChild("left", newChild)
        elif self.right is currentChild:
            return self.assignChild("right", newChild)

        return False

    #method to assign child based on balancing properties
    def assignChild(self, selectChild, child):
        if selectChild != "left" and selectChild != "right":
            return False
        if selectChild == "left":
            self.left = child
        else:
            self.right = child
        if child is not None:
            child.parent = self
        self.calculateHeight()
        return True

#AVL tree class
class avlTree:
    #AVL node constructor
    def __init__(self):
        self.root = None

    #method that performs left rotation
    def rotateLeft(self, node):
        right_leftChild = node.right.left

        if node.parent is not None:
            node.parent.updateChild(node, node.right)
        else:
            self.root = node.right
            self.root.parent = None


        node.right.assignChild('left', node)
        node.assignChild('right', right_leftChild)

        return node.parent

    #method that performs the right rotation
    def rotateRight(self, node):

        left_rightChild = node.left.right

        if node.parent is not None:
            node.parent.updateChild(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        node.left.assignChild('right', node)

        node.assignChild('left', left_rightChild)
        return node.parent

    #method that decides what balance to perform to maintain its balanced tree property
    def rebalance(self, node):
        node.calculateHeight()
        if node.getBalance() == -2:
            if node.right.getBalance() == 1:
                self.rotateRight(node.right)
            return self.rotateLeft(node)

        elif node.getBalance() == 2:
            if node.left.getBalance() == -1:
                self.rotateLeft(node.left)
            return self.rotateRight(node)

        return node

   #method that inserts a node into the AVL tree
    def insert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
        else:
            temp = self.root
            while temp is not None:
                if node.key < temp.key:
                    if temp.left is None:
                        temp.left = node
                        node.parent = temp
                        temp = None
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = node
                        node.parent = temp
                        temp = None
                    else:
                        temp = temp.right

            node = node.parent
            while node is not None:
                self.rebalance(node)
                node = node.parent

    #method used to traverse the tree and search a node with the desired key or word
    def search(self, key):
        temp = self.root
        while temp is not None:
            if temp.key.lower() == key.lower():
                return temp
            elif key > temp.key:
                temp = temp.right
            else: temp = temp.left
        return None

#node class for red black tree
class RBTNode:
    #constructor for node
    key = ""
    def __init__(self, key, parent, is_red = False, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

        if is_red:
            self.color = "red"
        else:
            self.color = "black"

    #method to check if both children share the color black property
    def are_both_children_black(self):
        if self.left != None and self.left.is_red():
            return False
        if self.right != None and self.right.is_red():
            return False
        return True

    #method to count
    def count(self):
        count = 1
        if self.left != None:
            count = count + self.left.count()
        if self.right != None:
            count = count + self.right.count()
        return count

    #method to acquire grandparent
    def get_grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    #methyod to get predecessor to current node
    def get_predecessor(self):
        node = self.left
        while node.right is not None:
            node = node.right
        return node

    #method to get sibling of current node
    def get_sibling(self):
        if self.parent is not None:
            if self is self.parent.left:
                return self.parent.right
            return self.parent.left
        return None

    #method to get uncle of current node
    def get_uncle(self):
        grandparent = self.get_grandparent()
        if grandparent is None:
            return None
        if grandparent.left is self.parent:
            return grandparent.right
        return grandparent.left

    #method to check if a node is black
    def is_black(self):
        return self.color == "black"

    #method to check if a node is red
    def is_red(self):
        return self.color == "red"

    #method to replace child
    def replace_child(self, current_child, new_child):
        if self.left is current_child:
            return self.set_child("left", new_child)
        elif self.right is current_child:
            return self.set_child("right", new_child)
        return False

    #method to set child when property is not met
    def set_child(self, which_child, child):
        if which_child != "left" and which_child != "right":
            return False

        if which_child == "left":
            self.left = child
        else:
            self.right = child

        if child != None:
            child.parent = self

        return True


#class for Red Black Tree
class redBlackTree:
    root = None
    #Red Black Tree Constructors
    def __init__(self):
        self.root = None

    def __len__(self):
        if self.root is None:
            return 0
        return self.root.count()

    #method to insert node into red black tree
    def insert(self, key):
        new_node = RBTNode(key, None, True, None, None)
        self.insert_node(new_node)

    #method to check red black properties before insertion
    def insert_node(self, node):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    if current_node.left is None:
                        current_node.set_child("left", node)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.set_child("right", node)
                        break
                    else:
                        current_node = current_node.right
        node.color = "red"
        self.insertion_balance(node)

    #method to balance tree
    def insertion_balance(self, node):
        if node.parent is None:
            node.color = "black"
            return

        if node.parent.is_black():
            return

        parent = node.parent
        grandparent = node.get_grandparent()
        uncle = node.get_uncle()

        if uncle is not None and uncle.is_red():
            parent.color = uncle.color = "black"
            grandparent.color = "red"
            self.insertion_balance(grandparent)
            return

        if node is parent.right and parent is grandparent.left:
            self.rotate_left(parent)
            node = parent
            parent = node.parent

        elif node is parent.left and parent is grandparent.right:
            self.rotate_right(parent)
            node = parent
            parent = node.parent

        parent.color = "black"
        grandparent.color = "red"

        if node is parent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    #method that performs left rotation
    def rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent != None:
            node.parent.replace_child(node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        node.right.set_child("left", node)
        node.set_child("right", right_left_child)

    #method that performs right rotation
    def rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent != None:
            node.parent.replace_child(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        node.left.set_child("right", node)
        node.set_child("left", left_right_child)

    #method to search for a word by key
    def search(self, key):
        current_node = self.root
        while current_node != None:

            if(current_node.key == key):
                return current_node

            elif key < current_node.key:
                current_node = current_node.left

            else:
                current_node = current_node.right
        return None

#global variable to be able to call the tree from any method or any instance
global tree

#method used to count the number of possible anagrams for a given word
def countAnagrams(word, dictionary,  wordList, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        currentNode = dictionary.search(str)
        if currentNode is not None:
            wordList.append(currentNode.key)
    else:
        for i in range(len(word)):
            cur = word [i: i + 1]
            before = word[0:i]
            after = word[i +1:]
            if cur not in before:
                countAnagrams(before + after, dictionary,  wordList, prefix + cur)
    return len(wordList)

#method fill an AVL tree
def avlFill(fileName, tree):
    file = open(fileName, "r")
    for line in file:
        current_line = line.split()
        if isinstance(tree, avlTree):
            tree.insert(Node(current_line[0]))
        else:
            tree.insert(current_line[0])
    file.close()

#method used to fill a red black tree
def redblackFill(fileName, tree):
    file = open(fileName, "r")
    for line in file:
        temp = line.split()
        tree.insert(temp[0])
    file.close()

#method provided by the lab to be able to create all possible word combinations
def print_anagram(word, dictionary, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        currentNode = dictionary.search(str)
        if currentNode is not None:
            print(currentNode.key)
    else:
        for i in range(len(word)):
            cur = word [i: i + 1]
            before = word[0:i]
            after = word[i +1:]
            if cur not in before:
                print_anagram(before + after, dictionary, prefix + cur)

#method to find the word with the maximum number of anagrams
def anagramMax(fileOfWords, tree):
    max = 0
    result = ""

    with open(fileOfWords, "r") as file:
        for line in file:
            wordList = []
            tempMax = countAnagrams(line.split()[0], tree, wordList)

            if tempMax > max:
                max = tempMax
                result = line.split()[0]
        print("The word with the most anagrams is %s."
              "\nIt has %d possible anagram combinations.\n" % (result, max))

#main method
def main():
    tree = avlTree()
    #menu design to interact with the user
    print("**************************Lab 3 Anagrams**************************")
    fileName = ""
    status = False
    while status is False:
        try:
            fileName = input("Please enter the file name excluding .txt "
                             "\nEnter No if you would like to use a default text file called text.txt: "
                             "\n")
            if(fileName.lower() == "no"):
                fileName = "text"
                status = True

            else:
                avlFill(fileName+".txt", tree)
                status = True

        except FileNotFoundError:
                print("File not found."
                      "\n")

    response = input("Would you like to use a AVL tree or a Red Black Tree: ")

    #loop to forcefully acquire a correct response
    while response.lower() != "avl tree" and response.lower() != "red black tree" and response.lower() != "red black" and response.lower() != "avl":
        response = input("please input a valid response: ")

    #perform AVL computations
    if response.lower() == "avl" or response.lower() == "avl tree":
        try:

                print("\n****************************************************************"
                      "\n                          AVL Tree"
                      "\n****************************************************************")
                avlFill(fileName+".txt", tree)

                word = input("\nPlease enter a word from the dictionary: ")
                print("\nThe available anagrams for the word %s are: " % (word))
                print_anagram(word, tree)
                wordList = []
                reps = countAnagrams(word,tree,wordList)
                print("\nThere is only %i possible combinations" % (reps))
        except FileNotFoundError:
            print("File not found."
                  "\n")
    #perform red black tree computations
    if response.lower() == "red black" or response.lower() == "red black tree":
         try:
                tree = redBlackTree()
                print("\n****************************************************************"
                      "\n                          Red Black Tree"
                      "\n****************************************************************")
                redblackFill(fileName+".txt", tree)

                word = input("\nPlease enter a word from the dictionary: ")
                print("\nThe available anagrams for the word %s are: " % (word))
                print_anagram(word, tree)
                wordList = []
                reps = countAnagrams(word,tree,wordList)
                print("\nThere is only %i possible combinations" % (reps))
         except FileNotFoundError:
            print("File not found."
                  "\n")
    #menu option to get max anagrams for desired word
    print("\n****************************************************************"
          "\n                        Max Anagrams"
          "\n****************************************************************"
          "\n")
    status = False
    while status is False:
        try:
            response = input("Please enter the file name excluding .txt "
                             "\nEnter No if you would like to use a default text file called text.txt: "
                             "\n")
            if(response.lower() == "no"):
                anagramMax("text.txt", tree)
                status = True
            else:
                anagramMax(response+".txt", tree)
                status = True
        except FileNotFoundError:
                print("File not found."
                      "\n")

#call main method
main()
#end of program

