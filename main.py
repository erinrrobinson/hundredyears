from pythonosc import udp_client
import argparse
from time import sleep
import os
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import freesound
import os
from os import path
from os import listdir
import shutil
from pydub import AudioSegment

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser.add_argument("--port2", default=6969,
                        help="The port the OSC server is listening on")
    parser.add_argument("--port", type=int, default=7402,
                        help="The port the OSC server is listening on")
    parser.add_argument("--port3", type=int, default=7500,
                        help="The port the OSC server is listening on")
    args = parser.parse_args()

ip = "127.0.0.1"
port = 7400


def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")
    if address in ['/sounds']:
        global searchword
        mydir = 'C:/Users/thewi/Desktop/sounds/'
        shutil.rmtree(mydir)
        os.mkdir(mydir)
        searchword = args
        client = freesound.FreesoundClient()
        client.set_token("KzaSVAUeKb29zvbEYQnOJgRIb5Yf3zQCcOaensfN")
        sounds = client.text_search(query=searchword, page_size=3, fields="id,name,previews", duration=(10, 20))
        sounds[0].retrieve_preview(mydir)
        sounds[1].retrieve_preview(mydir)
        sounds[2].retrieve_preview(mydir)
        print("sounds downloaded")
        filenum = 1
        for filename in os.listdir(mydir):
            dst = "poemsound" + str(filenum) + ".mp3"
            src = mydir + filename
            dst = mydir + dst

            # rename() function will rename all the files
            os.rename(src, dst)

            filenum += 1
        sound_count = 0
        AudioSegment.from_mp3("C:/Users/thewi/Desktop/sounds/poemsound1.mp3").export("C:/Users/thewi/Desktop/sounds/poemsound1.wav", format="wav")
        AudioSegment.from_mp3("C:/Users/thewi/Desktop/sounds/poemsound2.mp3").export("C:/Users/thewi/Desktop/sounds/poemsound2.wav", format="wav")
        AudioSegment.from_mp3("C:/Users/thewi/Desktop/sounds/poemsound3.mp3").export("C:/Users/thewi/Desktop/sounds/poemsound3.wav", format="wav")






dispatcher = Dispatcher()

dispatcher.set_default_handler(default_handler)


server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()
