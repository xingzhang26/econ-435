
from mrjob.job import MRJob
import MapReduce
import sys

mr = MapReduce.MapReduce()

class MRMutualFriends(MRJob):

    def mapper(self, _, line):
        # Your code here

    def reducer(self, key, values):
        # Your code here

if __name__ == '__main__':
    MRMutualFriends.run()
