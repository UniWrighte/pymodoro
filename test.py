import sys
import time
from pydub import AudioSegment
from pydub.playback import play

def test():
    for x in range(10):
        sys.stdout.write("\r")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write(str(10 - x)+ "    ")
        sys.stdout.flush()

#test()

sound = AudioSegment.from_ogg("./sonar.ogg")
play(sound)
play(sound)