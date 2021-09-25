from Haiku import Haiku
from Images import Images
from Sounds import Sounds
from datetime import datetime, timedelta


class Project:
    Haiku = None
    Images = None
    Sounds = None

    def __init__(self, search_word, num_files, timeout):
        self.SearchWord = search_word
        self.Num_Files = num_files
        self.Timeout = timeout
        self.generate_sounds()

    def generate_sounds(self):
        start = datetime.now()
        print('***Generating Sounds...***')
        self.Sounds = Sounds(self.SearchWord, self.Num_Files)
        print('***Finished generating Sounds in ' + str(datetime.now() - start) + ' seconds***')
