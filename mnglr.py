# image mangler by vvixi

# create glitch art from .bmp images
# results may vary with your source image
# good results can be achieved with the following bitmap settings:
# rgb, 8 bit, perceptual gamma sRGB

import random as r
import time
import math
from argparse import ArgumentParser
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
        try:
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
                        if rand in range(99):
                            line = b'rand'

                    case ["stretch"]:
                        if rand in range(7):
                            line *= rand

                    case ["stripper"]:
                        if rand in range(199):
                            line *= rand

                    case ["stutter"]:
                        if rand in range(999):
                            line += b'rand **99'

                    case ["shredder"]:
                        if rand % 2:
                            line *= rand

                    case ["ribbons"]:
                        if rand in range(22):
                            bytelist = list(line)
                            bytelist.reverse()
                            line = b'"".join(str(bytelist))'

                    case ["confetti"]:
                        # 22 previous
                        if rand % 7==0:
                            line = b'line.splitlines()[::-1]'

                    case ["confetti2"]:
                        if rand % 3==0:
                            line = b'line.splitlines()[randint(len(line))::]'
                            
                    case ["confetti3"]:
                        if rand in range(999):
                            line = b'line.splitlines()[::-1]'

                    case ["test"]:
                        if rand in range(199):
                            for char in line:
                                word = line.replace(char, r.randbytes(4))
                            line = b'word'

                # Write the processed line in the output file
                out.write(line)    
        except Exception:
            print("An error has occured.")

if __name__ == '__main__':
    # create the argparse instance
    parser = ArgumentParser(
                prog = 'Image Mangler',
                description = 'Create glitch art from bitmap images')
    parser.add_argument("-f", "--file", dest="input_file_name", help="input file name")

    parser.add_argument("-o", "--output", dest="output_file_name", help="specify output file name otherwise default to input file name with timestamp")

    parser.add_argument("-t", "--type", dest="dist_type", help="choose the type of distortion")

    args = parser.parse_args()
    #print(args.input_file_name, args.dist_type, args.output_file_name)
    glitch_image(args.input_file_name, args.dist_type)
