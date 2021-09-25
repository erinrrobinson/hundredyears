import freesound
import os
import pydub
import FileFolder



def convert_sounds(self):
        sound_count = 0
        for i in range(1, self.nSounds + 1):
            if FileFolder.does_file_exist(self.dir + 'haiku' + str(i) + '.mp3'):
                original_file = self.dir + 'haiku' + str(i) + '.mp3'
                converted_file = self.dir + 'haiku' + str(i) + '.wav'
                sound = pydub.AudioSegment.from_mp3(original_file)
                sound.export(converted_file, format="wav")
                sound_count += 1
        print('Number of sounds generated: ' + str(sound_count))