'''
Julio Hernandez
CS 2302
LAB #7 Dynamic Programming
Purpose: The objective of this lab is to implement the use of dynamic programming by using edit distance.
'''

#method to compute the number of changes
def editDistance(string, string2, length, length2):
    if length == 0:
        return length2

    if length2 == 0:
        return length
    #case for only one difference
    if string[length - 1] == string2[length2 -1]:
        return editDistance(string, string2, length -1, length2 -1)

    #step to compute all possible combinations
    return 1 + min(
                #Insert
                editDistance(string, string2, length , length2 - 1),
                #delete
                editDistance(string, string2, length - 1, length2),
                #replace
                editDistance(string, string2, length - 1, length2 - 1) )

#method to compare two strings
def compare(string, string2):
    print("******************************")
    print ("**********EDIT DISTANCE**********")
    print("Words:\n1) %s\n2) %s" %(string, string2))
    print("Edit Distance: %d" % editDistance(string, string2, len(string), len(string2)))

#main method
def main():
    case = False
    while case is False:
        response = input("Enter a word you would like to compare: ")

        try:
            #read file
            fileA = input("Enter the name of the first file excluding .txt: ")
            openedfileA = open(fileA + ".txt", "r").read().split(",")
            case = True

        except FileNotFoundError:
            print("\nFile not found\nPlease input a valid txt name")
        #read the file and compare words to input word
        for word in openedfileA:
            compare(response, word)

main()
