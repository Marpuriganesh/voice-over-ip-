import pyaudio
import socket

audio_rate = 44100
Audio_format = pyaudio.paInt16
no_of_channels = 1
frame_buffer = 1024
p = pyaudio.PyAudio()

stream = p.open(
    rate=audio_rate,
    format=Audio_format,
    channels=no_of_channels,
    input=True,
    frames_per_buffer=frame_buffer
)

ip = '127.0.0.1'
port = 35

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))
s.listen()

con, addr = s.accept()

print("connected to "+str(addr[0]))

while True:
    data = stream.read(frame_buffer)
    con.send(data)