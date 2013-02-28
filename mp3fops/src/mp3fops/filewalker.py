'''
Created on Feb 25, 2013

@author: jkunigk
'''
import os

class Filewalker(object):
    '''
    classdocs
    '''
    mp3_list = []
    
    def is_mp3(self, fname):
        if fname.lower().endswith('.mp3'):
            return True
        else:
            return False
        
    def dump_mp3_list(self):
        for mp3 in self.mp3_list:
            print(mp3)

    def make_mp3_list(self, paths, recurse, id3filter):
        for path in paths:       
            if os.path.isdir(path):
                if recurse:
                    for d, sub, files in os.walk(path):
                        for f in files:
                            if self.is_mp3(f) and id3filter.match(f):
                                self.mp3_list.add(os.path.join(d,f))
                else:
                    print("path is a directory and recurse is not set")  
                
                 
            else:
                if self.is_mp3(path) and id3filter.match(path):
                    self.mp3_list.append(path)
                        # If mp3 file && if it matches filter
                        # add it to global list of files tuse an fop on