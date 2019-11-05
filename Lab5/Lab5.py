'''
Julio Hernandez
88382550
CS 2302
Objective: The purpose of this lab is to obtain a set of numbers and sort them implementing a min heap data structure.
'''

#min heap class
class Heap:
    #class constructor to build an array
    def __init__(self):
        self.heapArr = []

    #method used to insert items in to the array
    def insert(self, key):
        self.heapArr.append(key)
        index = len(self.heapArr) - 1

        while index > 0:

            parentIndex = (index - 1) //2
            if (self.heapArr[index]>= self.heapArr[parentIndex]):
                return
            else:
                self.swap(parentIndex, index)
            index = parentIndex

    #method used to balance the min heap and sustain the min heap properties
    def heapify(self, i):
        n = len(self.heapArr)
        parent = i
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2

        #if statement to check if child is larger than the parent
        if leftChild < n and self.heapArr[i] > self.heapArr[leftChild]:
            parent = leftChild

        #if statement to check if child is larger than the parent
        if rightChild < n and self.heapArr[parent] > self.heapArr[rightChild]:
            parent = rightChild

        #parent is swapped if a larger value is found
        if parent != i:
            self.swap(i, parent)
            self.heapify(parent)

    #sort method to organize numbers in descending order
    def heapSort(self):
        size = len(self.heapArr)
        #temp array to hold the root item every time is is removed
        temp = []

        #for loop to traverse the array and pop the root into the temp array
        for i in range(size):
            temp.append(self.heapArr[0])
            self.swap(0, len(self.heapArr) - 1)
            self.heapArr = self.heapArr[:len(self.heapArr) - 1]
            self.heapify(0)

        #overwritting the heap array with the temp array
        self.heapArr = temp

    #method created to check if the heap array is empty
    def is_empty(self):
        return len(self.heapArr) == 0

    #method to extract the minimum value in the array
    def extract_min(self):
        if self.is_empty():
            return None

        #assign the value of the root to min
        #the root is now swapped and heapified
        #lastly the array is shortened by one
        min = self.heapArr[0]
        end = len(self.heapArr)-1
        self.swap(0, end)
        self.heapArr = self.heapArr[:end]
        self.heapify(0)

        #return the value of the smallest integer in the array
        return min

    #helper method used to print a heap array
    def print(self):
        print(self.heapArr)

        print("Length of the array: %d" % len(self.heapArr))

    #helper method to swap array values
    def swap(self, parent, child):
        self.heapArr[parent], self.heapArr[child] = self.heapArr[child], self.heapArr[parent]

#method used to read a txt file and insert it into a heap array
def read(heap):
    try:
        file = input("Enter file name, please exclude .txt: ")
        #method used to read the txt file
        read = open(file+".txt", "r").read().split(",")
        for i in read:
            #the value is hard coded into an integer
            entry = int(i)
            if entry >= 0:
                heap.insert(entry)
        return True
    except FileNotFoundError:
        #error for invalid input
        print("File not found. Please try again\n")
        return False
def menu():
    options = ["a", "b", "c", "d", "e", "f"]

    response = input("\nWhat would you like to do?"
                         "\nPlease select the desired letter option.\n"
                         "\nA) Display Min Heap of Inserted txt File"
                         "\nB) Insert Number"
                         "\nC) Extract Minimum Number"
                         "\nD) Check If Heap Is Empty"
                         "\nE) Sort the List"
                         "\nF) Exit\n")
    if response.lower() in options:
        return response.lower(), True
    else:
                print("Not a valid answer. Please try again.")
                return response, False
#main method
def main():
    #user interaction
    print("*****************************************************"
          "\n***************Min Heap Data Structure***************"
          "\n*****************************************************\n")
    #heap is created
    heap = Heap()
    #variable to check for correct inputs
    status = False

    #while loop to run continuously until correct input is inserted
    while status is False:
        status = read(heap)
    #variable used to keep the program running
    onoroff = True
    while onoroff is True:
        status = False
        while status is False:
            response, status = menu()

        #call method to print min heap array
        if response == "a":
            print("\nMin Heap List: \n")
            heap.print()
        #require user to input any number in to created heap
        if response == "b":
            status = False
            while status is False:
                response = input("Please enter a digit you wish to insert: ")
                try:
                    number = int(response)
                    heap.insert(number)
                    print("The new heap is: ")
                    heap.print()
                    print("\n")
                    status = True
                except ValueError:
                   print("Not a number. Please enter a valid number")

        #print the minimum number and print the new list
        if response == "c":
            minNumber = heap.extract_min()
            print("The minimum extracted is: %d\n" % minNumber)
            print("The new list is: ")
            heap.print()

        #call method to check in heap is empty
        if response == "d":
            answer = heap.is_empty()
            print(answer)

        #call method to sort min heap
        if response == "e":
            heap.heapSort()
            heap.print()

        #terminate the program and exit loop
        if response == "f":
            onoroff = False
    print("\nProgram is now closing.")


main()
#end of program

