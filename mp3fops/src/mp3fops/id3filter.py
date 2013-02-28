'''
Created on Feb 20, 2013

@author: jkunigk
'''
from mutagen.easyid3 import EasyID3

class Id3filter:
    id3filter = []
    # need a key-value thing here to implement the filter, so that traversing/matching it
    # is easy and standard list operators can be used
    def add_filter(self, key, val):
        self.id3filter.append([key, val])
    def dump_filter(self):
        for item in filter:
            print(str(item))
    def match(self, fname):
        id3tags = EasyID3(fname)
        for keyval in self.id3filter:
            key = keyval[0]
            val = keyval[1]
            if "".join(id3tags[key]) != val:
                return False
        return True
