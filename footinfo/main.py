############################################################################################################################################################
#
#       File Name   :   main.py
#
#       Description :   Get footinfo: table and injury information 
#
#       Author      :   Aniruth Oblah
#       
#
############################################################################################################################################################

import argparse 
from futinfo import table
from futinfo import injuries


def main():
    """
    Main method testing the futinfo module - containing tables & pl injuries 
    """
    print(table.get_table("england")) 
    print()
    #print(injuries.injuries_teams())
    print(injuries.get_injuries("liverpool"))

if __name__ == "__main__":
    main()
