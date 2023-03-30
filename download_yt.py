import json
from pytube import YouTube

yt = YouTube("http://youtube.com/watch?v=2lAe1cqCOXo")
video = yt.streams.get_lowest_resolution()
video.download(output_path="videos")


print(yt.title)
print(yt.description)
print(yt.keywords)
print(yt.views)
