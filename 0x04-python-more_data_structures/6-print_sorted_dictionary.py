#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    unsorted = list(a_dictionary.keys())
    unsorted.sort()
    for i in unsorted:
        print("{}:{}".format(i, a_dictionary.get(i)))
