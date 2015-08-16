#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################

def print_hist_old(h):
    for c in h:
        print c, h[c]  					# prints the key and its value


def print_hist_new(h):					# h is receiving d from hist_new
	for k, v in sorted(h.items()):      # items is a built in method that returns the key and value of h and then puts them in the variable k and v
		print (k, v)                    # This is the last function that will be called in the program so this line will be the output
    
  



##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################
def histogram_new(s):
    d = dict()
    for c in s:                 # Go through every item of the list
        d[c] = 1 + d.get(c, 0)  # For every occurrence of the item, it will add 1
    # return d                  # had I not called the print_hist_new below, I would return d. By calling the function, the return value is passed through the function
    
    print_hist_new(d)           

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    full_list = []
    with open('pledge.txt') as f:
        for line in f:
            line1 = line.split()
            full_list += line1
        # return full_list         # Use this if not calling histogram_new(full_list) below

    histogram_new(full_list)


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
##############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
    print get_pledge_list()     # Call the first funtion.

if __name__ == '__main__':
    main()
