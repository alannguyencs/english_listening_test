from constants import *
import database
from utils import util

db = database.load_database()

def show_database():
    for json_data in db:
        print(json_data['id'], json_data['title'])

def segment_caption():
    show_database()

    while(1):
        try:
            [file_id, begin_segment, end_segment] = input('Pick file id, begin segment, end segment: ').split(',')
            file_id = int(file_id)
            begin_segment = begin_segment.strip()
            end_segment = end_segment.strip()

            if file_id <= len(db):
                json_data = db[file_id]
                candidate_segments = util.retrieve_text(json_data['caption'], begin_segment, end_segment)
                print ("Candidate segments:")
                for segment_id, segment in enumerate(candidate_segments):
                    print (segment)
                    print (segment_id, ':', util.break_down_text(segment[0]))
                segment_id = int(input("Pick segment id: "))

                segment = candidate_segments[segment_id][0]
                print(util.break_down_text(segment))
                confirm = input('Confirm (y/n): ')
                if confirm == 'y':
                    return file_id, segment

        except Exception as error:
            print (error)
            pass

def segment_audio(file_id):
    json_data = db[file_id]
    mp3_path = AUDIO_PATH + json_data['title'] + '.mp3'
    sound = AudioSegment.from_file(mp3_path)

    while(1):
        try:
            [begin_time, end_time] = input('Pick begin time, end time: ').split(',')
            begin_time = begin_time.strip()
            end_time = end_time.strip()

            if len(begin_time) == 4: begin_time += '0'
            if len(end_time) == 4: end_time += '0'
            if len(begin_time) != 5 or len(end_time) != 5: continue

            m1, s1, t1 = int(begin_time[:2]), int(begin_time[2:4]), int(begin_time[4])
            m2, s2, t2 = int(end_time[:2]), int(end_time[2:4]), int(end_time[4])

            t1 = (m1 * 60 + s1 + (t1 + 1)//2) * 1000
            t2 = (m2 * 60 + s2 + (t2 + 1)//2) * 1000

            segment_sound = sound[t1:t2]
            segment_sound_path = SEGMENT_PATH + json_data['title'] \
                                 + '_' + begin_time \
                                 + '_' + end_time + '.mp3'
            segment_sound.export(segment_sound_path, format='mp3')

            confirm = input('Confirm (y/n): ')
            if confirm == 'y':
                return segment_sound_path


        except:
            pass

if __name__ == '__main__':
    while(1):
        file_id, caption = segment_caption()
        segment_text_path = segment_audio(file_id).replace('.mp3', '.txt')
        segment_text_file = open(segment_text_path, 'w')
        segment_text_file.write(caption + '\n')
        segment_text_file.close()

