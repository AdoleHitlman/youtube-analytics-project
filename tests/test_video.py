from src.video import Video, PLVideo


def test_video():
    video1 = Video('AWX4JnAnjBE')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_pl_video():
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

def test_broken_video_id():
    broken_video = Video('broken_video_id')
    assert broken_video.title is None
    assert broken_video.like_count is None