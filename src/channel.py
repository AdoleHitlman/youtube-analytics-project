from googleapiclient.discovery import build
import os
import json


class Channel:
    DEVELOPER_KEY = os.getenv('YT_API_KEY')
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    # конструктор
    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id

    # загрузка данных канала
    def __load(self):
        youtube = build(Channel.YOUTUBE_API_SERVICE_NAME, Channel.YOUTUBE_API_VERSION,
                        developerKey=Channel.DEVELOPER_KEY)
        channel = youtube.channels().list(part='snippet,statistics', id=self.channel_id).execute()

        self._title = channel['items'][0]['snippet']['title']
        self._video_count = channel['items'][0]['statistics']['videoCount']
        self._url = f'https://www.youtube.com/channel/{self.channel_id}'

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

    # сериализация в JSON
    def to_json(self, file_name: str) -> None:
        data = {
            'title': self.title,
            'video_count': self.video_count,
            'url': self.url
        }
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

            # получить экземпляр объекта youtube API

    @classmethod
    def get_service(cls):
        service = build(cls.YOUTUBE_API_SERVICE_NAME, cls.YOUTUBE_API_VERSION, developerKey=cls.DEVELOPER_KEY)
        return service