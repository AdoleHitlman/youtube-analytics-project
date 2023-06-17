from googleapiclient.discovery import build
import os
import json


class Channel:
    DEVELOPER_KEY = os.getenv('YT_API_KEY')
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    # конструктор
    def __init__(self, channel_id: str) -> None:
        self._channel_id = channel_id
        self.channel = Channel.youtube.channels().list(part='snippet,statistics,brandingSettings', id=channel_id).execute()
        self.playlists = Channel.youtube.playlists().list(channelId=channel_id,part='contentDetails,snippet',maxResults=50,).execute()

    def __str__(self) -> str:
        return f"{self.channel['items'][0]['snippet']['title']} (https://www.youtube.com/channel/{self._channel_id})"

    def __add__(self, other):
        channel2 = other.return_info()
        return int(self.channel['items'][0]['statistics']['subscriberCount']) + int(channel2['items'][0]['statistics']['subscriberCount'])

    def __sub__(self, other):
        channel2 = other.return_info()
        return int(self.channel['items'][0]['statistics']['subscriberCount']) - int(channel2['items'][0]['statistics']['subscriberCount'])

    def __gt__(self, other):
        channel2 = other.return_info()
        return int(self.channel['items'][0]['statistics']['subscriberCount']) > int(
            channel2['items'][0]['statistics']['subscriberCount'])

    def __ge__(self, other):
        channel2 = other.return_info()
        return int(self.channel['items'][0]['statistics']['subscriberCount']) >= int(channel2['items'][0]['statistics']['subscriberCount'])

    def __lt__(self, other):
        channel2 = other.return_info()
        return int(self.channel['items'][0]['statistics']['subscriberCount']) < int(channel2['items'][0]['statistics']['subscriberCount'])

    def __le__(self, other):
        channel2 = other.return_info()
        return int(self.channel['items'][0]['statistics']['subscriberCount']) <= int(channel2['items'][0]['statistics']['subscriberCount'])

    def __eq__(self, other):
        channel2 = other.return_info()
        return int(self.channel['items'][0]['statistics']['subscriberCount']) == int(channel2['items'][0]['statistics']['subscriberCount'])

    def print_info(self) -> dict:
        response = Channel.youtube.channels().list(
            part="snippet,statistics",
            id=self.channel_id
        ).execute()
        print(response)
        return response

    def return_info(self) -> dict:
        response = Channel.youtube.channels().list(
            part="snippet,statistics",
            id=self.channel_id
        ).execute()
        return response

    # свойство channel_id
    @property
    def channel_id(self) -> str:
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        raise AttributeError("channel_id cannot be modified")

    # загрузка данных канала
    def __load(self):
        self._title = self.channel['items'][0]['snippet']['title']
        self._video_count = self.channel['items'][0]['statistics']['videoCount']
        self._url = f'https://www.youtube.com/channel/{self.channel_id}'
        self._description = self.channel['items'][0]['snippet']['description']
        self._subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self._view_count = self.channel['items'][0]['statistics']['viewCount']

    # свойство title
    @property
    def title(self) -> str:
        if not hasattr(self, '_title'):
            self.__load()
        return self._title

    # свойство video_count
    @property
    def video_count(self) -> int:
        if not hasattr(self, '_video_count'):
            self.__load()
        return self._video_count

    # свойство url
    @property
    def url(self) -> str:
        return self._url

    # свойство description
    @property
    def description(self) -> str:
        if not hasattr(self, '_description'):
            self.__load()
        return self._description

    # свойство subscriber_count
    @property
    def subscriber_count(self) -> int:
        if not hasattr(self, '_subscriber_count'):
            self.__load()
        return self._subscriber_count

    # свойство view_count
    @property
    def view_count(self) -> int:
        if not hasattr(self, '_view_count'):
            self.__load()
        return self._view_count

    # сериализация в JSON
    def to_json(self, file_name: str) -> None:
        data = {
            'title': self.title,
            'video_count': self.video_count,
            'url': self.url,
            'description': self.description,
            'subscriber_count': self.subscriber_count,
            'view_count': self.view_count
        }
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # получить экземпляр объекта youtube API

    @classmethod
    def get_service(cls):
        service = build(cls.YOUTUBE_API_SERVICE_NAME, cls.YOUTUBE_API_VERSION, developerKey=cls.DEVELOPER_KEY)
        return service

    # список видео на канале
    def videos(self):
        youtube = Channel.get_service()
        videos = []
        next_page_token = None
        while True:
            request = youtube.search().list(
                part="id,snippet",
                channelId=self.channel_id,
                type='video',
                maxResults=50,
                order='date',
                pageToken=next_page_token
            )
            response = request.execute()
            videos += response['items']
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
        return videos
