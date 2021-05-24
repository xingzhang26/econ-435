from mrjob.job import MRJob
import re

class MRUniqueWords(MRJob):

    def mapper(self, _, line):
        for word in re.sub("[^a-zA-Z]+"," ",line).lower().split():
            yield (len(word), word)

    def reducer(self, key, values):
        yield key, len(set(values))

if __name__ == '__main__':
    MRUniqueWords.run()
    