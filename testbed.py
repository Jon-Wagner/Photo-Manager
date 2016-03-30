import numpy as np
import argparse as ap
import csv

'''
A short implementation of a photo manager, to be used as a testbed for data handling and ui.
All using of data should be seperate from any actual IO. Goal is to be database agnostic for future use
'''

parser = ap.ArgumentParser()
parser.add_argument('-f', '--filepath', nargs = '?', default = 'test_data.csv', help = 'use the specified csv file as the database')
args = parser.parse_args()

data = np.ndarray(shape = ())
with open(args.filepath) as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        data.append(row)
print(data)