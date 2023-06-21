import requests
import os


class Video:
    def __init__(self, video_id):
        self.id = video_id
        DEVELOPER_KEY = os.getenv('YT_API_KEY')
        try:
            url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={DEVELOPER_KEY}"
            response = requests.get(url)
            self.data = response.json()
            self.title = self.data['items'][0]['snippet']['title']
            self.views_count = self.data['items'][0]['statistics']['viewCount']
            self.like_count = self.data['items'][0]['statistics']['likeCount']
            self.video_link = f"https://www.youtube.com/watch?v={video_id}"
        except (KeyError, requests.exceptions.RequestException,IndexError):
            self.title = None
            self.views_count = None
            self.like_count = None
            self.video_link = f"https://www.youtube.com/watch?v={video_id}"

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
