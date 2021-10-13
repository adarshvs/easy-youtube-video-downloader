from pytube import YouTube
video_url = str(input('enter URL : '))
video = YouTube(video_url)
stream = video.streams.get_highest_resolution()

stream.download()
