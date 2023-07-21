# script to download youtube audio

# Import the pytube module
from pytube import YouTube

# Define the URL of the video
# url = "https://youtu.be/-hxeDjAxvJ8"
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# Create a YouTube object
yt = YouTube(url)

# Get the first stream that contains only audio
stream = yt.streams.filter(only_audio=True).first()

# Download the stream as an mp3 file
stream.download(filename="audio.mp3")

