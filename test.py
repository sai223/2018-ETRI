import os
import sys
import argparse
import pdb
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--filename", type=str, default='.', help="filename")
ap.add_argument("--gogo", type=bool, default=True)

args = ap.parse_args()

print(args)

if args.gogo==True:
	print('No problem')
