import os
import sys
from entropycalc import *



def scrapeDirectory(directory, outputfile, chunksize):
    for filename in os.listdir(directory):
        print "scraping " + directory + filename
        entropy_of_file_chunks(directory + filename, chunksize, outputfile)

def scrapeDirectoryTotals(directory, outputfile):
    outfile = open(outputfile, "w")
    for filename in os.listdir(directory):
        print "scraping " + directory + filename
        entropy = entropy_of_file(directory + filename)
        filesize = os.stat(directory + filename).st_size
        filetype = os.path.splitext(filename)[1]

        string = filename + ", " + filetype + ", " + str(entropy) + ", " + str(filesize) + ", " + "\n"
        outfile.write(string)
    outfile.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print sys.argv[0] + " takes as arguments:"
        print "    input_dir     - input directory to calculate entropy"
        print "    output_file   - the file to put the entropy calculations in."
        print "                    It is formatted as a CSV."
        print "    size_of_chunk - Optional - size of chunk to calculate on."
        print "                    If not present, calculates over whole file."
        exit()
    input_dir = sys.argv[1]
    output_file = sys.argv[2]
    if len(sys.argv) > 3:
        size_of_chunk = sys.argv[3]
        scrapeDirectory(input_dir, output_file, size_of_chunk)
    scrapeDirectoryTotals(input_dir, output_file)
