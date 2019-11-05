#Julio Hernandez
#88382550
#CS2301
#TTR 1:30

import os
import random

#method provided, it used to determine what is a directory and what is a file
#ultimately it was not used
def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list

#method provided, it is used to calculate if the image is a dog or a cat
def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2

#method to populate the pet arrays
def process_dir(path):

    #provided but not used
    #dir_list, file_list = get_dirs_and_files(path)
    cat_list = []
    dog_list = []

    # Your code goes here

    #according to many online sources os.walk traverses the directory recursively
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            #call method to evaluate image
            value = classify_pic((os.path.join(root,filename)))
            #add to list according to the value and filter non jpg files
            if value < .5 and ".jpg" in filename:
                cat_list.append((os.path.join(root,filename)).replace("\\", "/")) #replace is used to counter double backslashes
            if value > .5 and ".jpg" in filename:
                dog_list.append((os.path.join(root,filename)).replace("\\", "/"))

    #return the populated lists
    return cat_list, dog_list



def main():
    start_path = r'C:\Pictures' # current directory #r was added to try to counter double back slashes

    #method call and lists are created
    catList, dogList = process_dir(start_path)

    print(catList)
    print(dogList)


main()
