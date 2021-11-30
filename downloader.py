# import pytube
# importing module
from pytube import YouTube
# get link from user
url = 'https://youtu.be/7BXJIjfJCsA'
my_video = YouTube(url)

print("############# video title #################")
#get video title
print(my_video.title)
