import pafy
from datetime import datetime
from constants import *

query_file = list(open('../new_url.txt', 'r'))
query_list = [query_item.strip() for query_item in query_file]

track_file = list(open('../track.txt', 'r'))
track_list = [track_item.strip() for track_item in track_file]
url_head = "https://www.youtube.com/watch?v="

for url in query_list:
    if len(url) == 11 and url not in track_list:
        url_full = url_head + url

        video = pafy.new(url_full)
        print (video.title)
        video_title = video.title.replace('?', '')
        month_date = datetime.today().strftime('%m%d')

        best_audio_stream = video.getbestaudio()
        audio_path = AUDIO_PATH + month_date + '_' + video_title + '.' + best_audio_stream.extension
        best_audio_stream.download(audio_path)

        track_list.append(url)

track_file = open('../track.txt', 'w')
for url in track_list:
    track_file.write(url + '\n')
track_file.close()


