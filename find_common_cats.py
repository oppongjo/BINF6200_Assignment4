#!/usr/bin/env python3
# find_common_cats.py
"""
This program count the numbers of the categories and sort it
in ascending order, and then add the description to it
"""

import argparse
from assignment4 import io_utils


def main():
    """Business Logic"""
    args = get_cli_args()
    infile1 = args.infile1
    infile2 = args.infile2
    fh_in = io_utils.get_filehandle(infile1, "r")
    fh_in2 = io_utils.get_filehandle(infile2, "r")
    fh_out = io_utils.get_filehandle("OUTPUT/categories.txt", "w")
    counts = get_occurrences_with_dict(fh_in)
    disc = get_description_with_dict(fh_in2)
    print_result(counts, disc, fh_out)


def get_occurrences_with_dict(fh_in):
    """
Create a dictionary to store the categories from
chr21_genes.txt and sort it in ascending order
    """
    counts = {}
    lines = fh_in.readlines()[1:]
    for line in lines:
        categories = line.replace("\n", "").split("\t")[2]
        counts[categories] = counts.get(categories, 0) + 1
        sorted_dict = sorted(counts.items())
    return dict(sorted_dict) 


def get_description_with_dict(fh_in2):
    """
Create a dictionary to store the description from chr21_genes_categories.txt
    """
    disc = {}
    lines = fh_in2.readlines()
    for line in lines:
        description = line.replace("\n", "").split("\t")[1]
        categories = line.replace("\n", "").split("\t")[0]
        disc[categories] = description
    return disc


def print_result(counts, disc, fh_out):
    """
print out the results in a format
    """
    fh_out.write("Category\tOccurrence\tDescription\n")
    for key1, value1 in counts.items():
        for key2, value2 in disc.items():
            if key1 == key2:
                fh_out.write(f"{key1}\t\t{value1}\t\t{value2}\n")


def get_cli_args():
    """
Just get the command line options using argparse
@return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Combine on gene name \
and count the category occurrence')
    parser.add_argument('-i1', '--infile1', dest='infile1',
type=str, help='Path to the gene description file to open',
required=False, default='./chr21_genes.txt')
    parser.add_argument('-i2', '--infile2', dest='infile2',
type=str, help='Path to the gene category to open',
required=False, default='./chr21_genes_categories.txt')

    return parser.parse_args()


if __name__ == '__main__':
    main()
