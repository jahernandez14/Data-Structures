#Julio Hernandez
#88382550
#Lab 1
#This lab is designed to traverse a file directory and file jpg images.

import os
import random

#method provided, it used to determine what is a directory and what is a file
def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list
#static lists are created to store list information
class petList:
    catList = []
    dogList = []

#method provided, it is used to calculate if the image is a dog or a cat
def classify_pic(path):
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2

#method to populate the pet arrays
def process_dir(path):
    #Base call to avoid errors or paths that do no exist
    if path is None:
        return
    #creation of list with directories and files at current level
    dir_list, file_list = get_dirs_and_files(path)

    #pet arrays are created
    cat_list = []
    dog_list = []

    #for loop to traverse a given path and sort each file
    for x in file_list:
        #method to classify each file
        value = classify_pic(x)
        #if statement to filter dog or cat and also only accept jpg file types
        if value < .5 and ".jpg" in x:
            #add to list with full path
            cat_list.append((path + "/" + x).replace("\\", "/"))
        if value > .5 and ".jpg" in x:
            dog_list.append((path + "/" + x).replace("\\", "/"))
    #add the values of the list to a static list
    petList.catList += cat_list
    petList.dogList += dog_list

    #traverse all the folders of any given path
    for y in dir_list:
        #use a recursive call to filter the files to each folder
        process_dir(path + "/" + y)

    return cat_list, dog_list


def main():
    start_path = 'C:\Pictures' # current directory

    #method to begin filtering at the given path location
    process_dir(start_path)

    #print lists created
    print(petList.catList)
    print(petList.dogList)

#main method
main()
