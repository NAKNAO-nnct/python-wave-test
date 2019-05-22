import numpy as np
import wavio

waveFile = wavio.read("timpani.wav")
fs = waveFile

rate = waveFile.rate
width = waveFile.sampwidth
bit = 8 * width
data = waveFile.data

channel = len(waveFile.data[0, :])

print('rate: ', rate)
print('channel: ', channel)
print('width: ', width)


arr = np.empty((0, 2), int)

for i in range(len(data)):
    a = int(data[i][0] * 0.8)
    b = int(data[i][1] * 0.8)
    arr = np.append(arr, np.array([[a, b]]), axis=0)

# print(arr)
wavio.write('timpani-vooff.wav', arr, rate, sampwidth=width)
