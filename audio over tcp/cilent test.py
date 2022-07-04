import pyaudio
import socket

ip = "127.0.0.1"
port = 35

audio_rate = 44100
Audio_format = pyaudio.paInt16
no_of_channels = 1
frame_buffer = 1024
p = pyaudio.PyAudio()

stream = p.open(
    rate=audio_rate,
    format=Audio_format,
    channels=no_of_channels,
    output=True,
    frames_per_buffer=frame_buffer
)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))

while True:
    data = s.recv(1024)
    stream.write(data)
    print(data)