###################################################################################################################################################
#
#       File Name       :   add_to_redis_list.py
#
#       Description     :   Adds each line in a file to a redis list
#
#
#       Revision History
#       _______________________________________________________________________________________________________________________________________
#
#       No.     Author              Date                Version             Comments
#       _______________________________________________________________________________________________________________________________________
#
#       1       Aniruth Oblah       Apr 21, 2017        1.0                 Initial Version
#
# 
#################################################################################################################################################

import redis


def get_file_contents():
    """
    Get all lines from the specified file, store it in a list and return it.  
    """

    filename = "facts.txt"
    file_pointer = open(filename, "r", encoding='utf8', errors="ignore")
    file_list = file_pointer.readlines()
    
    return file_list


def add_list_to_redis(file_list):
    """
    Add list to redis set
    """
    setname = "facts"
    red = redis.Redis(host = 'localhost', db = 0)
    for item in file_list:
        item = item.strip("\n")
        red.sadd(setname, item)

def main():
    """
    Main method
    """
    print("Adding File content to Redis List")
    file_list = get_file_contents()
    add_list_to_redis(file_list)
    print("DONE!")



if __name__ == '__main__':
    main()
