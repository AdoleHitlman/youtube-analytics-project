import datetime
from src.playlist import PlayList
pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')

def test_title():
    assert pl.title == "Moscow Python Meetup №81"
def test_url():
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

duration = pl.total_duration
def test_duration():
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0
def test_show_best_video():
    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"