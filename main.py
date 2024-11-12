from yt_dlp import YoutubeDL

# Configure options if necessary
ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
}

with YoutubeDL(ydl_opts) as ydl:
    url = input('Please Enter URL: \n')
    print(ydl.download(url))