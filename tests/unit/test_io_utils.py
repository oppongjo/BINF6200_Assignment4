#!/usr/bin/python3
"""
Test suite for io_utils.py
"""

import os
import pytest
from assignment4.io_utils import get_filehandle

# pylint: disable=C0116
# pylint: disable=C0103

FILE_2_TEST = 'chr21_genes.txt'
FILE_LINES = \
    """
TPTE    tensin, putative protein-tyrosine phosphate, EC 3.1.3.48. 1.1
CYC1LP4 cytochrome c pseudogene 5
Pseudo1 putative zinc finger protein pseudogene 5

PRED1   putative gene, protein kinase C ETA type (EC 2.7.1.) like 3.2
ORLP1   pheromone receptor pseudogene 5
    """


def test_existing_get_filehandle_4_reading():

    # does it open a file for reading

    test = get_filehandle(FILE_2_TEST, 'r')
    assert hasattr(test, 'readline') is True, \
        'Not able to open for reading'


def test_existing_get_filehandle_4_writing():

    # does it open a file for writing

    test = get_filehandle('test.txt', 'w')
    assert hasattr(test, 'write') is True, \
        'Not able to open for writing'
    test.close()
    os.remove('test.txt')


def test_get_filehandle_4_IOError():

    # does it raise IOError

    with pytest.raises(IOError):
        get_filehandle('does_not_exist.txt', 'r')


def test_get_filehandle_4_OSError():
    # does it raise OSError

    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_4_ValueError():

    # does it raise ValueError

    with pytest.raises(ValueError):
        get_filehandle('wrong_open_mode.txt', 'rrr')



    
