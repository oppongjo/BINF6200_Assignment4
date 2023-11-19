#!/usr/bin/env python
# gene_names_from_chr21.py

import argparse
from assignment4 import io_utils


def main():
    "" "Business Logic"""
    args = get_cli_args()
    infile = args.infile
    fh_in = io_utils.get_filehandle(infile, "r")
    desc = create_dic(fh_in)
    while True:
        gene = input("\nEnter gene name of interest. Type quit to exit: ").lower()
        if gene in desc:
            print(f"{gene} found! Here is the description:")
            print(f"{desc[gene]}")
        elif gene == 'quit':
            print(f"Thanks for querying the data.")
            break
        else:
            print("Not a valid gene name.")


def create_dic(fh_in):
    """"
    create a dictionary to store the categories and descriptions of genes
    """
    desc = {}
    lines = fh_in.readlines()[1:]
    for line in lines:
        gene = line.strip().split("\t")[0].lower()
        description = line.strip().split("\t")[1].lower()
        desc[gene] = description
    return desc

def get_cli_args():
    """"
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, \
and ask user for a gene name')
    parser.add_argument('-i', '--infile', dest='infile', type=str, help='Path to the file to open',
    required=False, default='./chr21_genes.txt')
    return parser.parse_args()

if __name__ == "__main__":
    main()

