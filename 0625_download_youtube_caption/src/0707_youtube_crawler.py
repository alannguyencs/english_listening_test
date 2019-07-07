from constants import *
from utils import util
import database


db = database.load_database()
file_cnt = len(db)
url_existed = [json_data['url'] for json_data in db]
url_list = list(open(URL_NEW_PATH, 'r'))

for url in url_list:
    url = url.strip()
    if url in url_existed:
        continue
    url_full = YOUTUBE_PREFIX + url

    video = pafy.new(url_full)
    video_title = video.title
    for invalid_char in INVALID_CHARS:
        video_title = video_title.replace(invalid_char, '')
    print (video_title)

    timestamp = datetime.today().strftime('%y%m%d')

    best_audio_stream = video.getbestaudio()
    audio_path = AUDIO_PATH + timestamp + '_' + video_title + '.' + best_audio_stream.extension
    best_audio_stream.download(audio_path)

    sound = AudioSegment.from_file(audio_path)
    mp3_path = AUDIO_PATH + timestamp + '_' + video_title + '.' + '.mp3'
    sound.export(mp3_path, format="mp3", bitrate="128k")
    os.remove(audio_path)

    json_data = OrderedDict()
    json_data['id'] = util.num2str(file_cnt)
    json_data['url'] = url
    json_data['title'] = timestamp + '_' + video_title
    json_path = DATABASE_PATH + json_data['id'] + '.json'
    with open(json_path, 'w') as json_file:
        json.dump(json_data, json_file)

    file_cnt += 1
