#!/usr/bin/env python
import sys
import argparse
"""
this program will open one FASTA file and generate two files
One of the files generated contains protein sequence while the other contains the secondary structure
The program tell the user how many sequences were found for each of the output files and prints them to STDERR
"""


def main():
    """Business Logic"""
    args = get_cli_args()
    infile, mode = args.infile, 'r'
    fh_in = get_filehandle(infile, mode)
    pdb_protein_fh = get_filehandle('pdb_protein.fasta', 'w')
    pdb_ss_fh = get_filehandle('pdb_ss.fasta', 'w')
    list_headers, list_seqs = get_fasta_lists(fh_in)
    seq_count, ss_count = 0, 0
    for i, header in enumerate(list_headers):
        if header.endswith('sequence'):
            pdb_protein_fh.write(header + '\n')
            pdb_protein_fh.write(list_seqs[i]+'\n')
            seq_count += 1
        elif header. endswith('secstr'):
            pdb_ss_fh.write(header + '\n')
            pdb_ss_fh. write(list_seqs[i]+'\n')
            ss_count += 1
    print('Found {} protein sequences'.format(seq_count))
    print('Found {} ss sequences' .format(ss_count))
    pdb_protein_fh.close()
    pdb_ss_fh.close()


def get_filehandle(infile, mode):
    """get the file handle"""
    try:
        file_handle = open(infile, mode=mode)
        return file_handle
    except IOError as error:
        print('cannot open', infile)
        raise error
    except OSError as error:
        print('cannot open', infile)
        raise error
    except ValueError as error:
        print('wrong open mode')
        raise error


def get_fasta_lists(fh_in):
    """"Return header list and sequence list"""
    list_headers = []
    list_seqs = []
    lines = fh_in.readlines()
    for idx, line in enumerate(lines):
        # use .rstrip to get rid of the empty space and \n at the end of str
        line = line.rstrip()
        if line.startswith('>'):
            header_line = line
            list_headers.append(header_line)
            s_idx = idx + 1
            sequence = ''
            while s_idx < len(lines) and not lines[s_idx].startswith('>'):
                # use replace to only get rid of the In at the end of str
                sequence += lines[s_idx].replace("\n", "")
                s_idx += 1
            if sequence != '':
                list_seqs.append(sequence)
            else:
                continue
    if _verify_lists(list_headers, list_seqs):
        return list_headers, list_seqs


def _verify_lists(list_headers, list_seqs):
    if len(list_headers) != len(list_seqs):
        sys.exit("The size of the sequences and the header lists is different \n"
                 "Are you sure the FASTA is in correct format")
    else:
        return True


def get_cli_args():
    """Just get the command line options using argparse
    @return: Instance of argparse arguments"""
    parser = argparse. ArgumentParser(
        description='Give the fasta sequence file name to do the splitting')
    parser. add_argument('-i', '--infile',
                         dest='infile', type=str, help='Path to the file to open',
                         required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
