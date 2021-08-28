from abc import ABC, abstractmethod


class YouTubeLib:
    @abstractmethod
    def list_videos():
        pass


class YouTubeService(YouTubeLib):
    def list_videos(self):
        return "some videos"


class YoutubeProxy(YouTubeLib):
    service = None
    list_cache = None

    def __init__(self, service: YouTubeLib):
        self.service = service

    def list_videos(self):
        if not self.list_cache:
            print(
                "Cache empty, getting videos from YouTube by actually calling the YouTube services...")
            self.list_cache = self.service.list_videos()
        else:
            print("Video list in the cache.")
        return self.list_cache


class YouTubeManager:
    service = None

    def __init__(self, service: YouTubeLib):
        self.service = service

    def list_videos(self):
        self.service.list_videos()


if __name__ == "__main__":
    svc = YouTubeService()
    proxy = YoutubeProxy(svc)
    manager = YouTubeManager(proxy)
    manager.list_videos()
    manager.list_videos()
