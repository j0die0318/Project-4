from pytube import YouTube

fileSizeInBytes = 0
MaxFileSize = 0

class Downloader:
    def __init__(self, url: str):
        self.url: str = url
        self.yt:YouTube = YouTube(url, #on_progress_callback=progress_func,
                                  #on_complete_callback=complete_func,
                                  use_oauth=False,
                                  allow_oauth_cache=True)

    def fetch_streams(self):
        streams = self.yt.streams
        for s in streams:
            print(s)
        return streams
    
    def download(self, itag: str):
        stream = self.yt.streams.get_by_itag(int(itag))
        stream.download()
