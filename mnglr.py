# image mangler by vvixi
import random as r
import time
import math
#from __future__ import division

from optparse import OptionParser
from random import randint

ts = time.time()
def glitch_image(input_file_name, dist_type):
    output_file_name = None
    if output_file_name is None:
        head, tail = input_file_name.split('.')
        output_file_name = '{}-{}.{}'.format(head, ts, tail)

    input_file_lines = open(input_file_name, 'rb').readlines()
    output_file = open(output_file_name, 'wb')

    with output_file as out:
        # skip first line to avoid header data
        for line_index in range(len(input_file_lines[:1])):
            line = input_file_lines[line_index]

            # modify only after the first 70 bytes
            line = line[:70] + (line[70:] * randint(1, 8))

            # Write first line
            out.write(line)

        input_file_lines = input_file_lines[1:]

        # iterate over each line 
        for line in input_file_lines:
            # Get a random value between 1 and 10000
            cur_line = 0
            rand = randint(2, len(input_file_lines))

            match dist_type:
                case ["slitscramble"]:
                    # print("Running in ", args, " mode")
                    if rand in range(99):
                        line = rand
                        cur_line += 1
                case ["stretch"]:
                    if rand in range(7):
                        line *= rand
                        cur_line += 1
                case ["stripper"]:
                    if rand in range(199):
                        line *= rand
                        cur_line += 1
                case ["stutter"]:
                    if rand in range(999):
                        line += b'rand **99'
                        cur_line += 1
                case ["shredder"]:
                    if rand % 2:
                        line *= rand
                        cur_line += 1
           
            # Write the processed line in the output file
            out.write(line)

if __name__ == '__main__':
    # Create the options parser instance
   
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="input_file_name",
                help="input file name", metavar="FILE")
    parser.add_option("-o", "--output", dest="output_file_name",
                help="specify output file name")
    parser.add_option("-t", "--type",
                action="store_false", dest="dist_type", default=True,
                help="choose type of distortion")

    (options, args) = parser.parse_args()
    # print("Type -h or --help to view available options.")
    print("options:", str(options))
    print("arguments:", args)
    glitch_image(options.input_file_name, args)