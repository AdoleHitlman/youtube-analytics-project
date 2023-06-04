from src.channel import Channel

moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_channel_print_info():
    expected_output = {'kind': 'youtube#channelListResponse',
                       'etag': 'ZqQa_XVsDa4OLR5Vx9R37yylYsg',
                       'pageInfo': {'totalResults': 1, 'resultsPerPage': 5},
                       'items': [{'kind': 'youtube#channel',
                                  'etag': 'V-m2_dzieACSseY1VVC2eXkkVHU',
                                  'id': 'UC-OVMPlMA3-YCIeg4z5z23A',
                                  'snippet': {'title': 'MoscowPython',
                                              'description': 'Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)',
                                              'customUrl': '@moscowdjangoru',
                                              'publishedAt': '2012-07-13T09:48:44Z',
                                              'thumbnails': {'default': {
                                                  'url': 'https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj',
                                                  'width': 88, 'height': 88},
                                                  'medium': {
                                                      'url': 'https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj',
                                                      'width': 240, 'height': 240},
                                                  'high': {
                                                      'url': 'https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj',
                                                      'width': 800, 'height': 800}},
                                              'localized': {'title': 'MoscowPython',
                                                            'description': 'Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)'
                                                            },
                                              'country': 'RU'
                                              },
                                  'statistics': {'viewCount': '2319191', 'subscriberCount': '26000',
                                                 'hiddenSubscriberCount': False, 'videoCount': '687'
                                                 }
                                  }
                                 ]
                       }
    assert moscowpython.print_info() == expected_output
