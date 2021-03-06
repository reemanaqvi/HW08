#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError		

def reverse_lookup_new(d, v):
    list_d = []
    for k in d:
    	if str(d[k]) == v:
    		list_d.append(k)
    	
    return list_d



##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################

def histogram_new(s):
    d = dict()
    for c in s:                 # Goes through every item of the list
        d[c] = 1 + d.get(c, 0)  # For every occurrence of the item, it will add 1
    return d                  # had I not called the print_hist_new below, I would return d. By calling the function, the value is returned through the function
    
            


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

    return full_list

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print reverse_lookup_new(pledge_histogram, "1")
    print reverse_lookup_new(pledge_histogram, "9")
    print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
