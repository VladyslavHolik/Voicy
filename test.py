import time
import os


name = "first note.wav"
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "./Records/" + name)
os.remove(path)
print(time.ctime())
