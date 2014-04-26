# Copyright 2014 - Sean Donovan

import argparse
import os
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import plot


#based on https://stackoverflow.com/questions/990477/how-to-calculate-the-entropy-of-a-file
def calc_entropy(array, size):
    entropy = 0.0
    for val in range(0, len(array)):
        p = array[val] / float(size)
        if (p > 0):
            entropy = entropy - p*math.log(p,2)
    return entropy

def entropy_of_file(filename):
    f = open(filename, "rb")
    bytes = [0] * 256

    for i in range(os.stat(filename).st_size):
        byte = f.read(1)
        bytes[ord(byte)] += 1
    return calc_entropy(bytes, os.stat(filename).st_size)

def entropy_of_file_chunks(filename, chunksize, outputfile):
    f = open(filename, "rb")
    outfile = open(outputfile, "a")
    filesize = os.stat(filename).st_size
    filetype = os.path.splitext(filename)[1]
    filename = os.path.basename(filename)

    for i in range(filesize/chunksize + 1):
        size_of_chunk = min(10000, filesize - (chunksize * (i)))
        bytes = [0] * 256
        if size_of_chunk == 0:
            continue
        for j in range(size_of_chunk):
            byte = f.read(1)
            bytes[ord(byte)] += 1
        entropy = calc_entropy(bytes, size_of_chunk)
        string = filename + ", " + filetype + ", " + str(entropy) + ", " + str(filesize) + ", " + str(size_of_chunk) + ", " + str(i) + "\n"
        outfile.write(string)
    outfile.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Look at this file")
    args = parser.parse_args()
    
    
    f = open(args.filename, "rb")
    bytes = [0]*256
    
    for i in range(os.stat(args.filename).st_size):
        byte = f.read(1)
        #    bytes[byte] += 1
        #    print "\"" + byte + "\""# + " " + ord(byte))
        bytes[ord(byte)] += 1
    

#for byte in f:
#    bytes[int(byte)] += 1

#for i in range(256):
#    print "bytes[" + str(i) +"] = " + str(bytes[i])
    print calc_entropy(bytes, os.stat(args.filename).st_size)

    plot.figsize(600, 300)
    p = plot.plot_hist(bytes, 1, color='red')
    plot.figstuff(title='byte counts for file', xlabel='Byte value', ylabel='Byte count', xlim=[0,255], fn="test.pdf")


