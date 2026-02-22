import sounddevice as sd
from scipy.io.wavfile import write
import time


freq = 44100   #need to be 2x of hearing freq of human ie 20,000 
channel = 2
duration = 60
name = input("Name Your Audio File: ")

print("Recording Press Ctrl+C to stop.")
start_time = time.time()   #find the starting point of the recording

try:
    recording = sd.rec(int(duration*freq),samplerate=freq,channels=channel)
    sd.wait()
    actual_duration = duration  
except KeyboardInterrupt:
    print("Stopping..")
    sd.stop()
    actual_duration = time.time() - start_time   #finds the actual length of recording

end_sample = int(actual_duration*freq)   #to find actual cutoff point we multiply duration by frequency aka samples per second 
trimmed_rec = recording[:end_sample]   #using slice to shorten the recording to the actual length of audio
write(f"{name}.wav",freq,trimmed_rec)