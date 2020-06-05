import wave
    """Module for working with files.wav."""
import threading
import pyaudio

chunk = 1024
format = pyaudio.paInt16
channels = 2
rate = 44100

class ShouldListen():
    """Bool program uses for defining status ( listening or not)."""

    def __init__(self):
        """Creating bool and threading.Lock."""
        self.bool = True
        self._lock = threading.Lock()

    def set_false(self):
        """Sets bool to false."""
        with self._lock:
            self.bool = False

    def get_value(self):
        """Returns bool."""
        with self._lock:
            return self.bool

should_listen = ShouldListen()

def record(name):
    """Begins to listen and then saves record."""
    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("* recording")

    frames = []

    while should_listen.get_value():
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("./Records/" + name + '.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def record_voice(name):
    '''
    Main function for record, starts daemon so that programm
    knows when to stop recording
    '''
    recording = threading.Thread(target=record, args=(name,),)
    recording.start()
    print("\nTo stop recording press Enter")
    input("")
    should_listen.set_false()
    recording.join()


def play_voice(name):
    """Main function for playing records."""
    wf = wave.open("./Records/" + name + ".wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(chunk)

    while (data != '')&(data != b''):
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()
