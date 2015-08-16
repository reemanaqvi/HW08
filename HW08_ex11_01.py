#!/usr/bin/env python
# Exercise 1  
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary, returning the dict.  It doesn't matter what the 
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
##############################################################################

def store_to_dict():
    with open('words.txt') as fin:
          words_dict = {word.strip() for word in fin} 
          return words_dict
    

    # or:
    # words_dict = {}
    # with open('words.txt') as fin:
    #     for item in fin:
    #         word = item.strip()
    #         words_dict[word] = word

    #     return words_dict
##############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    if "this" in words_dict:
        print "Yup."
    if "qwertyuiop" in words_dict:
        print "Hmm."

if __name__ == '__main__':
    main()
