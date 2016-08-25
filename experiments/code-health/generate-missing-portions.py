#!/usr/bin/env python3
"""
Generate all combinations and permutations of missing accounts.
"""
__author__ = "Martin Blais <blais@furius.ca>"

import sys


def gen_inputs(template, args):
    for mask in range(2 ** len(args)):
        actual_args = [arg if not (1<<i & mask) else ''
                       for i, arg in enumerate(args)]
        sys.stdout.write(template.format(*actual_args))

def main():
    import argparse, logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)-8s: %(message)s')
    parser = argparse.ArgumentParser(description=__doc__.strip())
    #parser.add_argument('filenames', nargs='+', help='Filenames')
    args = parser.parse_args()

    gen_inputs('  Assets:Account        {:7} {:3}\n',
               ['100.00', 'USD'])
    gen_inputs('  Assets:Account        {:7} {:3} @ {:7} {:3}\n',
               ['100.00', 'USD', '1.20', 'CAD'])
    gen_inputs('  Assets:Account        {:2} {:4} {{{:7} {:3}}}\n',
               ['10', 'HOOL', '100.00', 'USD'])
    gen_inputs('  Assets:Account        {:2} {:4} {{{:7} # {:7} {:3}}}\n',
               ['10', 'HOOL', '100.00', '9.95', 'USD'])
    gen_inputs('  Assets:Account        {:2} {:4} {{{:7} # {:7} {:3}}} @ {:7} {:3}\n',
               ['10', 'HOOL', '100.00', '9.95', 'USD', '120.00', 'USD'])



if __name__ == '__main__':
    main()