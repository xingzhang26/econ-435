import re
import sys

def map(value):
  return (len(value),value)

def reduce(pair):
  return (pair[0],len(set(pair[1])))

if __name__ == "__main__":

    # load file's words
    fp = open(sys.argv[1],"r")
    text = re.sub("[^a-zA-Z]+"," "," ".join(fp.readlines())).lower()
    fp.close()

    # map
    #
    #   Note: If you're unfamiliar with list comprehension in python,
    #   read the following line as
    #     "The set of map(v) such that v is an element of text.split()."
    mapd = [map(v) for v in text.split()]

    # shuffle 
    g = []
    for length in set([v[0] for v in mapd]):
        values_with_length = []
        for v in mapd: 
            if v[0] == length:
                values_with_length.append(v[1])
        g.append( (length, values_with_length) )

    # reduce
    info = [reduce(pair) for pair in g]

    # output
    print("XX number of distinct words with YYY letters\n")
    print("XX  YYY")
    print("\n".join(["{1:2d}  {0:3d}".format(r[1],r[0]) for r in info]))
