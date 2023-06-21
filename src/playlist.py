#from src.channel import Channel
import isodate
import os
import datetime

from googleapiclient.discovery import build


#import json
class PlayListMixin:
    DEVELOPER_KEY = os.getenv('YT_API_KEY')
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_dir = PlayListMixin.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails',
                                                                  maxResults=50, ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_dir['items']]
        self.channel_id = PlayListMixin.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=self.video_ids[0]).execute()['items'][0]['snippet'][
            "channelId"]
        self.playlist_info = PlayListMixin.youtube.playlists().list(channelId=self.channel_id, part='contentDetails,snippet',
                                                               maxResults=50, ).execute()
        self.title = self.playlist_info["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
        self.sec = 0
        for video in \
        PlayListMixin.youtube.videos().list(part='contentDetails,statistics', id=','.join(self.video_ids)).execute()[
            'items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            self.sec += duration.seconds
        self.total_duration = datetime.timedelta(seconds=self.sec)

class PlayList(PlayListMixin):
    def show_best_video(self):
        max_likes = 0
        best_video = None
        for video_id in self.video_ids:
            video_response = PlayList.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',id=video_id).execute()
            if int(video_response['items'][0]['statistics']['likeCount']) > max_likes:
                max_likes: int = int(video_response['items'][0]['statistics']['likeCount'])
        for video_id in range(len(self.video_ids)):
            video_response = PlayList.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',id=self.video_ids[video_id]).execute()
            if max_likes == int(video_response['items'][0]['statistics']['likeCount']):
                best_video = f"https://youtu.be/{self.video_ids[video_id]}"
        return best_video

