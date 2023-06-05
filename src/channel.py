from googleapiclient.discovery import build
import os

api_key = os.getenv('YT_API_KEY')

print(api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        """Выводит в консоль информацию о канале."""

    def print_info(self) -> None:
        youtube = build("youtube", "v3", developerKey=api_key)
        response = youtube.channels().list(part="snippet,statistics", id=self.channel_id).execute()
        print(response)
        return response
