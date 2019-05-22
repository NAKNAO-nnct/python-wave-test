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

fs = int(input('遮断周波数:'))

M = int(0.433 * rate / fs)
if M % 2 == 0:
    M += 1

arr = np.empty((0, 2), int)

for i in range(M):
    data = np.append(data, np.array([[data[i][0], data[i][1]]]), axis=0)

for i in range(len(data)):
    a = 0
    b = 0
    for j in range(M):
        a += int(data[i+j][0])
        b += int(data[i+j][1])
    arr = np.append(arr, np.array([[int(a/M), int(b/M)]]), axis=0)

wavio.write('timpani-sample.wav', arr, rate, sampwidth=width)
